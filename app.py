__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os
import tempfile
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Page config
st.set_page_config(
    page_title="Document Q&A with RAG",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .answer-box {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .source-box {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">📄 AI Document Q&A System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload any PDF and ask questions - powered by RAG & Gemini AI</div>', unsafe_allow_html=True)

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'document_name' not in st.session_state:
    st.session_state.document_name = None
if 'num_pages' not in st.session_state:
    st.session_state.num_pages = 0
if 'num_chunks' not in st.session_state:
    st.session_state.num_chunks = 0

# Sidebar
with st.sidebar:
    st.header("📤 Upload Document")
    
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
    
    if uploaded_file:
        st.success(f"✅ File: {uploaded_file.name}")
        
        # Process button
        if st.button("🔄 Process Document", use_container_width=True):
            with st.spinner("⚙️ Processing document..."):
                try:
                    # Save uploaded file temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        tmp_path = tmp_file.name
                    
                    # Load PDF
                    loader = PyPDFLoader(tmp_path)
                    documents = loader.load()
                    
                    # Split into chunks
                    text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size=1000,
                        chunk_overlap=200,
                        length_function=len
                    )
                    chunks = text_splitter.split_documents(documents)
                    
                    # Create embeddings
                    with st.spinner("🧠 Creating embeddings..."):
                        embeddings = HuggingFaceEmbeddings(
                            model_name="sentence-transformers/all-MiniLM-L6-v2"
                        )
                    
                    # Create vector store
                    with st.spinner("💾 Building knowledge base..."):
                        vector_store = Chroma.from_documents(
                            documents=chunks,
                            embedding=embeddings
                        )
                    
                    # Store in session state
                    st.session_state.vector_store = vector_store
                    st.session_state.document_name = uploaded_file.name
                    st.session_state.num_pages = len(documents)
                    st.session_state.num_chunks = len(chunks)
                    st.session_state.chat_history = []  # Reset history for new doc
                    
                    # Clean up
                    os.unlink(tmp_path)
                    
                    st.success("✅ Ready to answer questions!")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    # Document stats
    if st.session_state.vector_store is not None:
        st.divider()
        st.subheader("📊 Document Stats")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Pages", st.session_state.num_pages)
        with col2:
            st.metric("Chunks", st.session_state.num_chunks)
        
        st.metric("Questions Asked", len(st.session_state.chat_history))
        
        # Clear button
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

# Main area
if st.session_state.vector_store is not None:
    # Current document indicator
    st.info(f"📂 Current Document: **{st.session_state.document_name}**")
    
    # Question input
    st.subheader("💬 Ask a Question")
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        question = st.text_input(
            "Your question:",
            placeholder="e.g., What is the main topic of this document?",
            label_visibility="collapsed"
        )
    
    with col2:
        ask_button = st.button("🔍 Get Answer", use_container_width=True)
    
    # Process question
    if ask_button and question:
        with st.spinner("🤔 Analyzing document..."):
            try:
                # Retrieve relevant chunks
                retriever = st.session_state.vector_store.as_retriever(
                    search_kwargs={"k": 4}  # Get top 4 most relevant chunks
                )
                relevant_docs = retriever.invoke(question)
                
                # Combine context
                context = "\n\n".join([doc.page_content for doc in relevant_docs])
                
                # Create enhanced prompt
                prompt = f"""You are a helpful AI assistant analyzing a document. Based on the context below, answer the question accurately and concisely.

Context from document:
{context}

Question: {question}

Instructions:
- Answer based only on the provided context
- If the answer is not in the context, say "I cannot find this information in the document."
- Be specific and cite page numbers when relevant
- Keep the answer clear and concise

Answer:"""
                
                # Get answer from Gemini
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt)
                answer = response.text
                
                # Display answer in styled box
                st.markdown("### 🤖 Answer")
                st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
                
                # Show sources
                with st.expander("📚 View Source Context (Click to expand)"):
                    for i, doc in enumerate(relevant_docs, 1):
                        page_num = doc.metadata.get('page', 'Unknown')
                        st.markdown(f"**Source {i}** - Page {page_num}")
                        st.markdown(f'<div class="source-box">{doc.page_content[:400]}...</div>', unsafe_allow_html=True)
                        if i < len(relevant_docs):
                            st.divider()
                
                # Add to chat history
                st.session_state.chat_history.append({
                    "question": question,
                    "answer": answer,
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
                
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Chat history
    if st.session_state.chat_history:
        st.divider()
        st.subheader("📜 Previous Questions")
        
        # Reverse to show newest first
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            with st.container():
                st.markdown(f"**🕐 {chat['timestamp']}**")
                st.markdown(f"**Q:** {chat['question']}")
                st.markdown(f"**A:** {chat['answer']}")
                if i < len(st.session_state.chat_history) - 1:
                    st.divider()

else:
    # Welcome screen
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.info("👈 Upload a PDF from the sidebar to get started!")
        
        st.subheader("✨ Features")
        st.markdown("""
        - 📄 Upload any text-based PDF
        - 🧠 Powered by RAG (Retrieval Augmented Generation)
        - 🎯 Get accurate answers with source citations
        - 💬 Chat history tracking
        - ⚡ Fast and free!
        """)
        
        st.subheader("💡 Example Questions")
        st.markdown("""
        - What is the main topic of this document?
        - Summarize the key findings
        - What does it say about [specific topic]?
        - What are the conclusions?
        - Explain [concept] mentioned in the document
        """)
        
        st.subheader("🔧 How It Works")
        st.markdown("""
        1. **Upload** - Your PDF is loaded and processed
        2. **Chunk** - Document is split into manageable pieces
        3. **Embed** - Text is converted to vector embeddings
        4. **Retrieve** - Most relevant chunks are found for your question
        5. **Generate** - AI creates an answer based on context
        """)

# Footer
st.divider()
st.caption("Built with Streamlit, LangChain, ChromaDB & Google Gemini AI | RAG Architecture")

# 📄 AI Document Q&A System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)

**Live Demo:** [Try it here!](https://document-app-rag-hasitha.streamlit.app/)

AI-powered document question-answering system using Retrieval Augmented Generation (RAG) architecture. Upload any PDF and ask questions in natural language.

---

## 🎯 What It Does

Upload a PDF document and ask questions about it. The AI reads your document, finds relevant information, and provides accurate answers with source citations.

**Example:**
- Upload: Employee Handbook PDF
- Ask: "What's the work from home policy?"
- Get: Answer with page numbers and exact context

---

## ✨ Key Features

- 📄 **PDF Upload** - Supports text-based PDF documents
- 🧠 **RAG Architecture** - Retrieval Augmented Generation for accuracy
- 🎯 **Source Citations** - See which parts of the document were used
- 💬 **Chat Interface** - Ask multiple questions interactively
- ⚡ **Fast Processing** - Answers in 2-3 seconds
- 🆓 **Free to Use** - Powered by Google Gemini API

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | Google Gemini 2.5 Flash |
| **Framework** | LangChain |
| **Embeddings** | sentence-transformers/all-MiniLM-L6-v2 |
| **Vector Store** | ChromaDB |
| **PDF Processing** | PyPDF |
| **Frontend** | Streamlit |

---

## 🏗️ How RAG Works
```
1. 📄 Upload PDF
2. ✂️  Split into chunks (1000 chars each)
3. 🧠 Convert to embeddings (vector representations)
4. 💾 Store in ChromaDB vector database
5. ❓ User asks question
6. 🔍 Find most relevant chunks (semantic search)
7. 🤖 Send chunks + question to Gemini AI
8. ✅ Get answer with sources
```

**Why RAG vs Direct ChatGPT?**
- ✅ More accurate (grounded in YOUR documents)
- ✅ Cites sources (transparency)
- ✅ Works with private/internal docs
- ✅ No hallucination on document content

---

## 💼 Use Cases

**HR Teams:** Employee handbook Q&A, policy clarification  
**Legal:** Contract analysis, clause lookup  
**Customer Support:** Product manual queries, troubleshooting  
**Research:** Academic paper analysis, literature review  
**Sales:** Proposal analysis, RFP responses  

---

## 🚀 Try It Yourself

### Live Demo
👉 **[document-qa-rag.streamlit.app](https://document-app-rag-hasitha.streamlit.app/)**

### Run Locally
```bash
# Clone repository
git clone https://github.com/divyasrisruthi/document-qa-rag.git
cd document-qa-rag

# Install dependencies
pip install -r requirements.txt

# Set up API key
# Create .env file with:
# GEMINI_API_KEY=your_key_here

# Run app
streamlit run app.py
```

---

## 📊 Performance

- **Processing Time:** ~10 seconds for 50-page PDF
- **Response Time:** 2-3 seconds per question
- **Chunk Retrieval:** Top 4 most relevant chunks
- **Supported PDFs:** Text-based (not scanned documents)

---

## 🔮 Future Enhancements

- [ ] Multi-document support (query across multiple PDFs)
- [ ] Conversation memory (AI remembers previous questions)
- [ ] OCR support for scanned PDFs
- [ ] Export Q&A as report
- [ ] Advanced filtering by page range

---

## 📚 What I Learned

- RAG architecture and vector embeddings
- Semantic search with ChromaDB
- Prompt engineering for LLMs
- Document chunking strategies
- Production deployment with Streamlit Cloud

---

## ⚠️ Limitations

- Text-based PDFs only (scanned documents need OCR)
- Works best with well-structured documents
- Optimized for English language
- Large documents may need multiple queries

## 🙏 Acknowledgments

- **LangChain** - RAG framework
- **Google Gemini** - LLM API
- **Streamlit** - Web framework
- **sentence-transformers** - Embedding models

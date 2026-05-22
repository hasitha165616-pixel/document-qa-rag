# 📄 AI Document Q&A System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)](https://render.com/)

An AI-powered Document Question Answering System built using Retrieval Augmented Generation (RAG). Upload PDF documents and interact with them using natural language queries powered by semantic search and Google Gemini AI.

---

# 🚀 Live Demo

👉 https://document-qa-rag-gnsx.onrender.com

---

# 📌 Project Overview

This project allows users to upload PDF documents and ask questions about the content in natural language.

Instead of generating generic responses, the application uses RAG (Retrieval Augmented Generation) to retrieve relevant document sections before generating answers. This improves factual accuracy and reduces hallucinations.

The system combines:
- semantic vector search
- document chunking
- embeddings
- vector databases
- LLM-powered response generation

to provide contextual and accurate answers.

---

# ✨ Features

- 📄 Upload and process PDF documents
- 🧠 RAG-based AI question answering
- 🔍 Semantic similarity search
- 💬 Interactive chat interface
- ⚡ Fast contextual responses
- 📚 Context-grounded answers
- 🌐 Deployed on Render
- 🎯 User-friendly Streamlit interface

---

# 🛠️ Tech Stack

| Component | Technology |
|-----------|-------------|
| Language | Python |
| Frontend | Streamlit |
| Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| Vector Database | ChromaDB |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| PDF Processing | PyPDF |
| Deployment | Render |

---

# 🏗️ System Workflow

```text
1. User uploads PDF document
2. PDF text is extracted
3. Text is split into smaller chunks
4. Embeddings are generated for each chunk
5. Chunks are stored in ChromaDB
6. User asks a question
7. Relevant chunks are retrieved using semantic similarity
8. Retrieved context is sent to Gemini AI
9. AI generates contextual response
```

---

# 🧠 Why RAG?

Traditional AI systems may hallucinate or generate inaccurate responses.

Retrieval Augmented Generation (RAG) improves reliability by:
- grounding answers in actual document content
- retrieving relevant context before generation
- improving factual consistency
- enabling document-specific querying

This makes the system more accurate and trustworthy for real-world document analysis.

---

# 💼 Use Cases

### 📌 HR & Internal Documentation
- Employee handbook Q&A
- Company policy clarification
- Internal knowledge search

### 📌 Legal
- Contract clause lookup
- Compliance document analysis
- Policy interpretation

### 📌 Research & Education
- Academic paper querying
- Literature review assistance
- Study material summarization

### 📌 Customer Support
- Product documentation assistance
- Troubleshooting support
- FAQ automation

---

# 📂 Project Structure

```text
AI-Document-QA/
│
├── app.py
├── requirements.txt
├── README.md
├── chroma_db/
├── uploaded_docs/
└── utils/
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/hasitha165616-pixel/document-qa-rag.git
cd document-qa-rag
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 4️⃣ Run Application Locally

```bash
streamlit run app.py
```

---

# 🌐 Deployment

This application is deployed using Render.

### Render Configuration

| Setting | Value |
|---|---|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

---

# 📊 Performance

- ⚡ Average response time: 2–3 seconds
- 📄 Supports text-based PDFs
- 🔍 Semantic retrieval using vector embeddings
- 💾 Efficient vector search with ChromaDB

---

# 🔮 Future Enhancements

- [ ] Multi-document querying
- [ ] OCR support for scanned PDFs
- [ ] Conversation memory
- [ ] Export Q&A sessions
- [ ] Multi-language support
- [ ] Authentication system

---

# 📚 Key Learnings

This project helped me gain practical experience in:
- Retrieval Augmented Generation (RAG)
- Vector databases and embeddings
- Semantic search systems
- LangChain pipelines
- Prompt engineering
- AI application deployment
- Streamlit-based UI development

---

# ⚠️ Limitations

- Supports only text-based PDFs
- Scanned documents require OCR support
- Large documents may increase processing time
- Optimized mainly for English-language documents

---

# 🙏 Acknowledgements

- LangChain
- Google Gemini API
- Streamlit
- ChromaDB
- HuggingFace Sentence Transformers
- Render

---

# 👩‍💻 Author

Developed by Hasitha

If you found this project useful, feel free to ⭐ the repository.

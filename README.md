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
- LLM-based response generation

to provide contextual and source-aware answers.

---

# ✨ Features

- 📄 Upload and process PDF documents
- 🧠 RAG-based AI question answering
- 🔍 Semantic similarity search
- 💬 Interactive chat interface
- ⚡ Fast contextual responses
- 📚 Context-grounded answers
- 🌐 Web deployment with Render
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

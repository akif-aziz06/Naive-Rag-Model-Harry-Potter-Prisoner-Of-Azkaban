# ⚡ Harry Potter RAG System - Prisoner of Azkaban

This project is a **Retrieval-Augmented Generation (RAG)** system designed to answer questions about the book *"Harry Potter and the Prisoner of Azkaban"*. It uses a vector database to store document chunks and a Large Language Model (LLM) to generate context-aware responses.

---

## 🚀 Features

- **PDF Text Extraction**: Automatically extracts text from PDF files using `PyPDF2`.
- **Intelligent Chunking**: Splits large book text into manageable chunks with overlap for better context preservation.
- **Persistent Vector Database**: Stores embeddings and text chunks in `ChromaDB` for fast semantic retrieval.
- **Groq-Powered LLM**: Uses the `Llama-3.1-8b-instant` model via Groq Cloud for ultra-fast response generation.
- **Interactive Chat UI**: A clean, user-friendly interface built with `Streamlit` to interact with the book's content.

---

## 📂 Project Structure

```text
HARRY-POTER-RAG-SYSTEM/
├── VECTOR-BD/
│   ├── 3 - Harry Potter and the Prisoner of Azkaban.pdf  # Source data
│   ├── extraction.py                                    # PDF reading utility
│   ├── ingestion.py                                     # Chunking and DB storage logic
│   ├── generation.py                                    # Streamlit UI and RAG pipeline
│   ├── requirements.txt                                 # Project dependencies
│   └── chroma_db_storage/                               # Persistent database files (auto-generated)
├── .env                                                 # Environment variables (API Keys)
└── README.md                                            # Project documentation
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.10 or higher.
- A **Groq API Key** (Get one at [Groq Console](https://console.groq.com/)).

### 2. Clone the Repository
```bash
git clone <your-repository-url>
cd HARRY-POTER-RAG-SYSTEM
```

### 3. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r VECTOR-BD/requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory and add your Groq API Key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📖 Usage

### Step 1: Ingest the Document
Run the ingestion script to process the PDF and populate the vector database:
```bash
python VECTOR-BD/ingestion.py
```
*This will create the `chroma_db_storage` folder.*

### Step 2: Launch the App
Start the Streamlit interface to begin chatting:
```bash
streamlit run VECTOR-BD/generation.py
```

---

## 🛠️ Technologies Used

- **Framework**: [Streamlit](https://streamlit.io/)
- **LLM API**: [Groq Cloud](https://groq.com/) (Llama 3.1)
- **Vector DB**: [ChromaDB](https://www.trychroma.com/)
- **PDF Parsing**: [PyPDF2](https://pypdf2.readthedocs.io/)
- **Environment**: `python-dotenv`

---

## ⚠️ Note
Please ensure you do not commit your `.env` file to public repositories to keep your API keys secure.
"# Naive-Rag-Model-Harry-Potter-Prisoner-Of-Azkaban" 

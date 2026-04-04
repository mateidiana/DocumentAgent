# Custom Knowledge Agent for Enterprise/University Documents

## Team Name
Diana Matei & Serb Paul

## Team Members
- Diana Matei
- Serb Paul

## Project Overview
This project implements a Multi-Tool Document Intelligence Agent that allows users to upload custom documents and interact with them through natural language queries. The system uses Retrieval-Augmented Generation (RAG) and an agent-based architecture to provide grounded answers, summaries, and document analysis. It is designed to support dynamic data ingestion, safe response generation, and evaluation of answer quality.

## Architecture Description

The system follows an agent-based architecture built around multiple functional modules that work together to process documents and answer user queries.

### 1. Data Ingestion Layer
This component is responsible for accepting new datasets such as PDFs, text files, or CSV files. Uploaded documents are parsed, cleaned, split into chunks, and prepared for indexing.

### 2. Chunking and Preprocessing
After ingestion, the text is divided into smaller overlapping chunks to preserve context and improve retrieval quality. Metadata such as file name, page number, and section information is stored together with each chunk.

### 3. Vector Database
The processed chunks are converted into embeddings and stored in a vector database. This enables semantic search over the uploaded documents and supports efficient retrieval of relevant context for user questions.

### 4. Retrieval Module
When the user submits a query, the retrieval module searches the vector database and returns the most relevant chunks. This module may also include keyword-based retrieval for exact-match queries.

### 5. LLM/SLM Generation Module
The retrieved document chunks are passed to a language model, which generates an answer grounded in the provided context. Depending on the implementation, this module may use a commercial LLM API or a fine-tuned small language model.

### 6. Agent Layer
The agent acts as the decision-making component of the system. Based on the user request, it decides which tool or module to use, such as retrieval, summarization, verification, or comparison. This allows the system to handle multiple document-related tasks more flexibly.

### 7. Safety and Verification Layer
To reduce hallucinations and unsafe outputs, the system includes mechanisms for answer verification, citation support, and toxicity filtering. If the retrieved evidence is insufficient, the system can return a fallback response instead of generating unsupported content.

### 8. User Interface
The frontend provides a simple interface for uploading documents and interacting with the system through a chat-based workflow. It displays the generated answer along with supporting sources or retrieved document chunks.

## Suggested Tech Stack
- **Frontend:** [Streamlit / Gradio / React]
- **Backend:** [Python / FastAPI]
- **Embeddings:** [Sentence Transformers / OpenAI Embeddings]
- **Vector Database:** [Chroma / FAISS]
- **Language Model:** [OpenAI / Gemini / Claude / Mistral / Phi]
- **Frameworks:** [LangChain / LlamaIndex / custom pipeline]

## Repository Structure
```text
[project-name]/
│── app.py
│── README.md
│── requirements.txt
│── data/
│── chroma_db/
│── src/
│   ├── ingest.py
│   ├── chunking.py
│   ├── retriever.py
│   ├── qa.py
│   ├── agent.py
│   └── evaluation.py
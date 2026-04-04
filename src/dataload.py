from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdfs(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            docs = loader.load()
            documents.extend(docs)

    return documents


docs = load_pdfs("../data/")
print(f"Loaded {len(docs)} pages")

from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    return chunks


chunks = chunk_documents(docs)
print(f"Created {len(chunks)} chunks")

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

from langchain_community.vectorstores import Chroma

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma_db"
)

vector_db.persist()

query = "What is this course about?"

results = vector_db.similarity_search(query, k=3)

for r in results:
    print(r.page_content[:300])
    print("----")
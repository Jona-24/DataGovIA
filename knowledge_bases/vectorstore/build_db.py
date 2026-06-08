from pathlib import Path

from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_ollama import OllamaEmbeddings


# ==========================
# Load Knowledge Unit
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ku_file = (
    BASE_DIR
    / "knowledge_bases"
    / "capabilities"
    / "KU_METADATA_MANAGEMENT_v1.0.md"
)

print(f"Loading: {ku_file}")

with open(
    ku_file,
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

documents = [
    Document(
        page_content=text,
        metadata={
            "source": "KU_METADATA_MANAGEMENT"
        }
    )
]

# ==========================
# Chunking
# ==========================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_documents(
    documents
)

print(f"Generated {len(chunks)} chunks")

# ==========================
# Embeddings
# ==========================

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# ==========================
# Chroma
# ==========================

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=str(
        BASE_DIR / "chroma_db"
    )
)

print(
    "Documents in collection:",
    db._collection.count()
)

print("Vector database created successfully")
print(f"Indexed chunks: {len(chunks)}")
print(
    f"Persisting to: {BASE_DIR / 'chroma_db'}"
)

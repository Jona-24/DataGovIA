from pathlib import Path

from langchain_community.vectorstores import Chroma

from langchain_ollama import OllamaEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory=str(
        BASE_DIR / "chroma_db"
    ),
    embedding_function=embeddings
)

results = db.similarity_search(
    "Metadata Management",
    k=3
)

for i, doc in enumerate(results):

    print()

    print("=" * 80)

    print(f"RESULT {i+1}")

    print("=" * 80)

    print(doc.page_content)
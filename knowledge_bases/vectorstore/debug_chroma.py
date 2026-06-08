from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

db = Chroma(
    persist_directory=str(
        BASE_DIR / "chroma_db"
    ),
    embedding_function=OllamaEmbeddings(
        model="nomic-embed-text"
    )
)

print(
    "Documents:",
    db._collection.count()
)

results = db.similarity_search(
    "metadata management",
    k=5
)

print(
    "Results:",
    len(results)
)

for r in results:
    print()
    print("=" * 80)
    print(r.page_content[:500])
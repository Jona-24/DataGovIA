from pathlib import Path

from langchain_community.vectorstores import Chroma

from langchain_ollama import OllamaEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def retrieval_agent(state):

    print("Running Retrieval Agent")

    capability_gaps = state.get(
        "capability_gaps",
        []
    )

    if not capability_gaps:

        state["retrieved_knowledge"] = []

        return state

    query = capability_gaps[0]

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = Chroma(
        persist_directory=str(
            BASE_DIR / "chroma_db"
        ),
        embedding_function=embeddings
    )

    data = db._collection.get()

    results = db.similarity_search(
        query,
        k=3
    )

    retrieved = []

    for doc in results:

        retrieved.append(
            doc.page_content
        )

    state["retrieved_knowledge"] = retrieved
    
    return state
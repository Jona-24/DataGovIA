from pathlib import Path

from langchain_community.vectorstores import Chroma

from langchain_ollama import OllamaEmbeddings


BASE_DIR = Path(__file__).resolve().parent.parent.parent


def retrieval_agent(state):

    print("Running Retrieval Agent")

    capability_gaps = state.capability_gaps

    if not capability_gaps:

        state.retrieved_knowledge = []

        return state

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = Chroma(
        persist_directory=str(
            BASE_DIR / "chroma_db"
        ),
        embedding_function=embeddings
    )

    retrieved = []

    for gap in capability_gaps:

        print(f"Retrieving knowledge for: {gap}")

        results = db.similarity_search(
            gap,
            k=2
        )

        for doc in results:

            if doc.page_content not in retrieved:

                retrieved.append(
                    doc.page_content
                )

    state.retrieved_knowledge = retrieved

    return state
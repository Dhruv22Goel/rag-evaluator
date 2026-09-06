import chromadb
from chromadb.utils import embedding_functions


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.embedding_function = (
            embedding_functions.DefaultEmbeddingFunction()
        )

        self.collection = self.client.get_or_create_collection(
            name="rag_documents",
            embedding_function=self.embedding_function
        )

    def add_chunks(self, chunks: list[str]):
        ids = [f"chunk_{i}" for i in range(len(chunks))]

        self.collection.add(
            documents=chunks,
            ids=ids
        )

    def search(self, query: str, top_k: int = 3) -> list[str]:
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
        )

        return results["documents"][0]
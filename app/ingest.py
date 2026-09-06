from app.document_loader import load_document
from app.chunker import chunk_text
from app.services.vector_store import VectorStore


def ingest_document(file_path: str):
    text = load_document(file_path)

    chunks = chunk_text(text)

    vector_store = VectorStore()
    vector_store.add_chunks(chunks)

    return len(chunks)
def chunk_text(
    text: str,
    chunk_size: int = 200,
    chunk_overlap: int = 40,
) -> list[str]:

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks

if __name__ == "__main__":
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    chunks = chunk_text(
        sample,
        chunk_size=10,
        chunk_overlap=3,
    )

    for index, chunk in enumerate(chunks, start=1):
        print(f"Chunk {index}: {chunk}")
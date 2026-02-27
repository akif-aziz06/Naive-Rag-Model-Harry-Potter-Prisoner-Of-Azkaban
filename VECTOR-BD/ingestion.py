import chromadb
from extraction import extract_text_from_pdf

def ingest_document(file_path):
    print(f"Extracting text from {file_path}...")
    pdf_text = extract_text_from_pdf(file_path)

    print("Chunking text...")
    chunk_size = 1000      
    chunk_overlap = 100    
    chunks = []

    # Using basic Python math to slice the text
    for i in range(0, len(pdf_text), chunk_size - chunk_overlap):
        chunk = pdf_text[i : i + chunk_size]
        chunks.append(chunk)

    print("Initializing Persistent ChromaDB and storing chunks...")
    # Critical Change: Using PersistentClient to save the database to disk
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "chroma_db_storage")
    chroma_client = chromadb.PersistentClient(path=db_path)
    collection = chroma_client.get_or_create_collection(name="harry_potter_rag")

    chunk_ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        ids=chunk_ids
    )

    print("\n PDF processed and permanently stored in Chroma DB. System is ready!\n")

# Run this script directly to build your database
if __name__ == "__main__":
    ingest_document("3 - Harry Potter and the Prisoner of Azkaban.pdf")
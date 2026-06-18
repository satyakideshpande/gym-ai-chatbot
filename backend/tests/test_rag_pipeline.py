# Test file to demonstrate the RAG pipeline: chunking + embedding + storage + retrieval

import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).parent.parent
sys.path.insert(0, str(backend_path))

from app.services.rag.chunker import load_and_chunk_data
from app.services.rag.embedder import create_embeddings_with_chunks
from app.services.rag.vector_store import VectorStore
from app.services.rag.retriever import Retriever


def test_rag_pipeline():
    """
    End-to-end test of the RAG pipeline:
    1. Load and chunk the gym data
    2. Generate embeddings for each chunk
    3. Store chunks + embeddings in ChromaDB
    4. Retrieve similar chunks for a sample query
    """
    print("=" * 80)
    print("RAG PIPELINE TEST: Chunking → Embedding → Storage → Retrieval")
    print("=" * 80)
    
    # Step 1: Get chunks from the data
    print("\n[STEP 1] Loading and chunking data...")
    chunks = load_and_chunk_data(verbose=False)
    print(f"✓ Got {len(chunks)} chunks from gym data")
    
    # Step 2: Generate embeddings
    print("\n[STEP 2] Generating embeddings...")
    embeddings, generator = create_embeddings_with_chunks(chunks)
    
    # Step 3: Store in ChromaDB
    print("\n[STEP 3] Storing chunks and embeddings in ChromaDB...")
    
    # Define vector DB path relative to backend directory
    vector_db_path = backend_path / "vector_db"
    
    vector_store = VectorStore(db_path=str(vector_db_path), collection_name="gym_data")
    vector_store.clear_collection()  # Clear previous data
    vector_store.store_embeddings(chunks, embeddings)
    
    stats = vector_store.get_stats()
    print(f"✓ Storage complete. Total chunks stored: {stats['total_chunks']}")
    
    # Step 4: Retrieve similar chunks for sample queries
    print("\n[STEP 4] Testing retrieval with sample queries...")
    print("-" * 80)
    
    retriever = Retriever(db_path=str(vector_db_path), collection_name="gym_data")
    
    # Test queries
    test_queries = [
        "What equipment is available at the gym?",
        "Tell me about gym membership",
        "What are the gym's operating hours?"
    ]
    
    for query_idx, query in enumerate(test_queries, 1):
        print(f"\n{'='*80}")
        print(f"QUERY {query_idx}: {query}")
        print(f"{'='*80}")
        
        results = retriever.search_similar(query, top_k=3)
        
        print(f"\n✓ Retrieved {len(results)} relevant chunks")
    
    print("\n" + "=" * 80)
    print("RAG PIPELINE TEST COMPLETED SUCCESSFULLY")
    print("=" * 80)
    print(f"\nVector database stored at: {vector_db_path.absolute()}")
    print("Chunks are now ready for retrieval in your LLM API!")


if __name__ == "__main__":
    test_rag_pipeline()

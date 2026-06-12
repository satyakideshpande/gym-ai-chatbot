# Test file to demonstrate the RAG pipeline: chunking + embedding

import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).parent.parent
sys.path.insert(0, str(backend_path))

from app.services.rag.chunker import load_and_chunk_data
from app.services.rag.embedder import create_embeddings_with_chunks


def test_rag_pipeline():
    """
    End-to-end test of the RAG pipeline:
    1. Load and chunk the gym data
    2. Generate embeddings for each chunk
    3. Display results
    """
    print("=" * 60)
    print("RAG PIPELINE TEST: Chunking + Embedding")
    print("=" * 60)
    
    # Step 1: Get chunks from the data
    print("\n[STEP 1] Loading and chunking data...")
    chunks = load_and_chunk_data(verbose=False)
    print(f"✓ Got {len(chunks)} chunks from gym data")
    
    # Step 2: Generate embeddings
    print("\n[STEP 2] Generating embeddings...")
    embeddings, generator = create_embeddings_with_chunks(chunks)
    
    # Step 3: Display sample results
    print("\n[STEP 3] Sample Results:")
    print("-" * 60)
    
    # Show first 3 chunks and their embeddings
    for i in range(min(3, len(chunks))):
        print(f"\nChunk {i + 1}:")
        print(f"  Text: {chunks[i][:100]}..." if len(chunks[i]) > 100 else f"  Text: {chunks[i]}")
        print(f"  Embedding (first 10 dims): {embeddings[i][:10]}")
        print(f"  Embedding shape: {len(embeddings[i])} dimensions")
    
    print("\n" + "=" * 60)
    print("RAG PIPELINE TEST COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    test_rag_pipeline()

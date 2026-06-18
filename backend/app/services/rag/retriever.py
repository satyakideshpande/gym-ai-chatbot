# Retrieval layer for ChromaDB
# Searches and retrieves relevant chunks based on queries

import chromadb
from pathlib import Path


class Retriever:
    """Retrieve relevant chunks from ChromaDB based on similarity search."""
    
    def __init__(self, db_path: str = "vector_db", collection_name: str = "gym_data"):
        """
        Initialize ChromaDB client and load collection.
        
        Args:
            db_path: Directory where ChromaDB files are stored
            collection_name: Name of the collection to query
        """
        db_dir = Path(db_path)
        
        if not db_dir.exists():
            raise ValueError(f"Database path does not exist: {db_dir}")
        
        print(f"Loading ChromaDB from: {db_dir.absolute()}")
        
        # Initialize persistent ChromaDB client
        self.client = chromadb.PersistentClient(path=str(db_dir))
        
        # Get collection
        self.collection = self.client.get_collection(name=collection_name)
        
        print(f"Loaded collection: {collection_name}")
        print(f"Total chunks in collection: {self.collection.count()}")
    
    def search_similar(self, query: str, top_k: int = 3):
        """
        Search for similar chunks based on a query string.
        
        Args:
            query: User's question or search query
            top_k: Number of similar chunks to return
            
        Returns:
            List of similar chunks with metadata
        """
        print(f"\nSearching for similar chunks to: '{query}'")
        print(f"Retrieving top {top_k} results...")
        
        # Query the collection
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        
        # Format results
        retrieved_chunks = []
        
        if results and results['documents'] and len(results['documents']) > 0:
            for i, (chunk_text, distance) in enumerate(
                zip(results['documents'][0], results['distances'][0])
            ):
                # Convert distance to similarity score (lower distance = higher similarity)
                similarity_score = 1 - distance
                
                retrieved_chunks.append({
                    'rank': i + 1,
                    'text': chunk_text,
                    'similarity': similarity_score,
                    'distance': distance
                })
                
                print(f"\n  Rank {i + 1}:")
                print(f"    Similarity: {similarity_score:.4f}")
                print(f"    Text: {chunk_text[:80]}..." if len(chunk_text) > 80 else f"    Text: {chunk_text}")
        else:
            print("  No results found!")
        
        return retrieved_chunks
    
    def get_combined_context(self, query: str, top_k: int = 3, separator: str = "\n\n---\n\n") -> str:
        """
        Search and combine top-k chunks into a single context string.
        Useful for passing to LLM as context.
        
        Args:
            query: User's question
            top_k: Number of chunks to retrieve
            separator: String to separate chunks
            
        Returns:
            Combined context string from all retrieved chunks
        """
        chunks = self.search_similar(query, top_k)
        
        if not chunks:
            return ""
        
        context = separator.join([chunk['text'] for chunk in chunks])
        return context

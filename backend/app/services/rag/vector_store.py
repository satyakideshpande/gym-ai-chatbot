# Vector database storage layer using ChromaDB
# Stores chunks and their embeddings for fast retrieval

import chromadb
from pathlib import Path


class VectorStore:
    """Store and manage embeddings in ChromaDB."""
    
    def __init__(self, db_path: str = "vector_db", collection_name: str = "gym_data"):
        """
        Initialize ChromaDB client and collection.
        
        Args:
            db_path: Directory to store ChromaDB files
            collection_name: Name of the collection to use
        """
        # Create vector_db directory if it doesn't exist
        db_dir = Path(db_path)
        db_dir.mkdir(exist_ok=True)
        
        print(f"Initializing ChromaDB at: {db_dir.absolute()}")
        
        # Initialize persistent ChromaDB client
        self.client = chromadb.PersistentClient(path=str(db_dir))
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}  # Use cosine similarity
        )
        
        print(f"Connected to collection: {collection_name}")
    
    def store_embeddings(self, chunks: list, embeddings):
        """
        Store chunks and their embeddings in ChromaDB.
        
        Args:
            chunks: List of text chunks
            embeddings: Numpy array of embeddings from SentenceTransformers
        """
        print(f"\nStoring {len(chunks)} chunks in ChromaDB...")
        
        # Convert embeddings to list format if needed
        embeddings_list = embeddings.tolist() if hasattr(embeddings, 'tolist') else embeddings
        
        # Prepare data for ChromaDB
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        metadatas = [{"chunk_index": i} for i in range(len(chunks))]
        
        # Add to collection
        self.collection.add(
            ids=ids,
            embeddings=embeddings_list,
            documents=chunks,
            metadatas=metadatas
        )
        
        print(f"✓ Successfully stored {len(chunks)} chunks")
    
    def get_stats(self) -> dict:
        """
        Get statistics about the stored data.
        
        Returns:
            Dictionary with collection stats
        """
        count = self.collection.count()
        return {
            "total_chunks": count,
            "collection_name": self.collection.name
        }
    
    def clear_collection(self):
        """Clear all data from the collection."""
        print(f"Clearing collection: {self.collection.name}")
        # Delete the collection and recreate it
        self.client.delete_collection(name=self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            metadata={"hnsw:space": "cosine"}
        )
        print("✓ Collection cleared")

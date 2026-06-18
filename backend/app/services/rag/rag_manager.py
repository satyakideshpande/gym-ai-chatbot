# RAG Manager - Orchestrates the complete RAG pipeline
# Handles initialization, chunking, embedding, storage, and retrieval

import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(backend_path))

from app.services.rag.chunker import load_and_chunk_data
from app.services.rag.embedder import create_embeddings_with_chunks
from app.services.rag.vector_store import VectorStore
from app.services.rag.retriever import Retriever


class RAGManager:
    """
    Manages the complete RAG pipeline:
    - Initialization (chunking, embedding, storage)
    - Retrieval for queries
    """
    
    def __init__(self, db_path: str = "vector_db", collection_name: str = "gym_data"):
        """
        Initialize RAG Manager.
        
        Args:
            db_path: Directory for ChromaDB storage
            collection_name: Name of the ChromaDB collection
        """
        self.db_path = db_path
        self.collection_name = collection_name
        self.vector_store = None
        self.retriever = None
        self.is_initialized = False
    
    def initialize(self, verbose: bool = True):
        """
        Initialize the RAG pipeline by chunking, embedding, and storing data.
        Should be called once on application startup.
        
        Args:
            verbose: If True, print progress information
        """
        if self.is_initialized:
            if verbose:
                print("RAG pipeline already initialized")
            return
        
        # Initialize vector store first
        self.vector_store = VectorStore(db_path=self.db_path, collection_name=self.collection_name)
        
        # Check if collection already has data
        existing_stats = self.vector_store.get_stats()

        print(
            f"Found existing collection with "
            f"{existing_stats['total_chunks']} chunks"
        )

        if existing_stats['total_chunks'] > 0:
            if verbose:
                print("\n" + "="*60)
                print("RAG PIPELINE INITIALIZATION")
                print("="*60)
                print(f"✓ Using existing collection with {existing_stats['total_chunks']} chunks")
                print("="*60)
            self.is_initialized = True
            self.retriever = Retriever(db_path=self.db_path, collection_name=self.collection_name)
            return
        
        if verbose:
            print("\n" + "="*60)
            print("INITIALIZING RAG PIPELINE")
            print("="*60)
        
        try:
            # Step 1: Load and chunk data
            if verbose:
                print("\n[Step 1] Loading and chunking gym data...")
            chunks = load_and_chunk_data(verbose=False)
            if verbose:
                print(f"✓ Created {len(chunks)} chunks")
            
            # Step 2: Generate embeddings
            if verbose:
                print("\n[Step 2] Generating embeddings...")
            embeddings, _ = create_embeddings_with_chunks(chunks)
            if verbose:
                print(f"✓ Generated embeddings for {len(embeddings)} chunks")
            
            # Step 3: Store in ChromaDB
            if verbose:
                print("\n[Step 3] Storing in ChromaDB...")
            self.vector_store.store_embeddings(chunks, embeddings)
            
            stats = self.vector_store.get_stats()
            if verbose:
                print(f"✓ Stored {stats['total_chunks']} chunks in ChromaDB")
            
            # Step 4: Initialize retriever
            if verbose:
                print("\n[Step 4] Loading retriever...")
            self.retriever = Retriever(db_path=self.db_path, collection_name=self.collection_name)
            
            self.is_initialized = True
            if verbose:
                print("\n" + "="*60)
                print("✓ RAG PIPELINE INITIALIZED SUCCESSFULLY")
                print("="*60)
        
        except Exception as e:
            print(f"✗ Error initializing RAG pipeline: {e}")
            raise
    
    def retrieve_context(self, query: str, top_k: int = 3, verbose: bool = False) -> str:
        """
        Retrieve relevant context for a user query.
        
        Args:
            query: User's question
            top_k: Number of chunks to retrieve
            verbose: If True, print retrieval details
            
        Returns:
            Combined context string from top-k chunks
        """
        if not self.is_initialized:
            raise RuntimeError("RAG pipeline not initialized. Call initialize() first.")
        
        if verbose:
            print(f"\nRetrieving context for: '{query}'")
        
        context = self.retriever.get_combined_context(query, top_k=top_k)
        
        if verbose:
            print(f"✓ Retrieved {top_k} relevant chunks as context")
        
        return context
    
    def get_status(self) -> dict:
        """
        Get the status of the RAG pipeline.
        
        Returns:
            Dictionary with status information
        """
        return {
            "initialized": self.is_initialized,
            "db_path": self.db_path,
            "collection_name": self.collection_name,
            "total_chunks": self.vector_store.get_stats()['total_chunks'] if self.vector_store else 0
        }


# Global RAG Manager instance
_rag_manager = None


def get_rag_manager(db_path: str = "vector_db") -> RAGManager:
    """
    Get or create the global RAG Manager instance.
    
    Args:
        db_path: Directory for ChromaDB storage
        
    Returns:
        RAGManager instance
    """
    global _rag_manager
    if _rag_manager is None:
        _rag_manager = RAGManager(db_path=db_path)
    return _rag_manager


def initialize_rag(db_path: str = "vector_db", verbose: bool = True):
    """
    Initialize the RAG pipeline (call on app startup).
    
    Args:
        db_path: Directory for ChromaDB storage
        verbose: If True, print progress information
    """
    manager = get_rag_manager(db_path)
    manager.initialize(verbose=verbose)

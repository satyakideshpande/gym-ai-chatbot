# Embedding generation using SentenceTransformers
# Converts text chunks into numerical vectors for semantic search

from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    """Generate embeddings for text chunks using SentenceTransformers."""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding generator with a pre-trained model.
        
        Args:
            model_name: Name of the SentenceTransformers model to use
                       "all-MiniLM-L6-v2" - fast, lightweight (384 dims)
                       "all-mpnet-base-v2" - better quality (768 dims)
                       See: https://www.sbert.net/docs/pretrained_models.html
        """
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        print(f"Model loaded successfully. Embedding dimension: {self.model.get_sentence_embedding_dimension()}")
    
    def generate_embeddings(self, chunks: list) -> list:
        """
        Generate embeddings for a list of text chunks.
        
        Args:
            chunks: List of text strings
            
        Returns:
            List of embeddings (numpy arrays converted to lists)
        """
        print(f"\nGenerating embeddings for {len(chunks)} chunks...")
        embeddings = self.model.encode(chunks, show_progress_bar=True)
        print(f"Generated {len(embeddings)} embeddings")
        return embeddings
    
    def get_embedding_stats(self, embeddings: list) -> dict:
        """
        Get statistics about the generated embeddings.
        
        Args:
            embeddings: List of embedding vectors (numpy array)
            
        Returns:
            Dictionary with stats like dimension, count, etc.
        """
        if len(embeddings) == 0:
            embedding_dim = 0
        else:
            # embeddings is a 2D numpy array, get the dimension of each embedding
            embedding_dim = embeddings[0].shape[0] if hasattr(embeddings[0], 'shape') else len(embeddings[0])
        
        return {
            "total_embeddings": len(embeddings),
            "embedding_dimension": embedding_dim,
            "model": self.model.get_sentence_embedding_dimension()
        }


def create_embeddings_with_chunks(chunks: list) -> tuple:
    """
    Convenience function to create embeddings from chunks.
    
    Args:
        chunks: List of text chunks
        
    Returns:
        Tuple of (embeddings, embedding_generator)
    """
    generator = EmbeddingGenerator()
    embeddings = generator.generate_embeddings(chunks)
    stats = generator.get_embedding_stats(embeddings)
    
    print(f"\nEmbedding Statistics:")
    print(f"  Total embeddings: {stats['total_embeddings']}")
    print(f"  Embedding dimension: {stats['embedding_dimension']}")
    
    return embeddings, generator

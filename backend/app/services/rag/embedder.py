# Embedding generation using SentenceTransformers
# Converts text chunks into numerical vectors for semantic search


class EmbeddingGenerator:
    """Generate embeddings for text chunks using SentenceTransformers."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding generator with a pre-trained model.

        Args:
            model_name: Name of the SentenceTransformers model to use
                       "all-MiniLM-L6-v2" - fast, lightweight (384 dims)
                       "all-mpnet-base-v2" - better quality (768 dims)
        """

        # Lazy import
        from sentence_transformers import SentenceTransformer

        print(f"Loading embedding model: {model_name}")

        self.model = SentenceTransformer(model_name)

        print(
            f"Model loaded successfully. Embedding dimension: "
            f"{self.model.get_sentence_embedding_dimension()}"
        )

    def generate_embeddings(self, chunks: list):
        """
        Generate embeddings for a list of text chunks.
        """

        print(f"\nGenerating embeddings for {len(chunks)} chunks...")

        embeddings = self.model.encode(
            chunks,
            show_progress_bar=True
        )

        print(f"Generated {len(embeddings)} embeddings")

        return embeddings

    def get_embedding_stats(self, embeddings) -> dict:

        if len(embeddings) == 0:
            embedding_dim = 0
        else:
            embedding_dim = (
                embeddings[0].shape[0]
                if hasattr(embeddings[0], "shape")
                else len(embeddings[0])
            )

        return {
            "total_embeddings": len(embeddings),
            "embedding_dimension": embedding_dim,
            "model": self.model.get_sentence_embedding_dimension()
        }


def create_embeddings_with_chunks(chunks: list):

    generator = EmbeddingGenerator()

    embeddings = generator.generate_embeddings(chunks)

    stats = generator.get_embedding_stats(embeddings)

    print("\nEmbedding Statistics:")
    print(f"  Total embeddings: {stats['total_embeddings']}")
    print(f"  Embedding dimension: {stats['embedding_dimension']}")

    return embeddings, generator
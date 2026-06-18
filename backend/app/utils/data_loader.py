# Helper utilities to load knowledge base files

from pathlib import Path


def read_gym_data() -> str:
    """
    Reads the gym knowledge base file from the knowledge_base folder.
    
    Returns:
        str: Content of the gym data file, or None if not found
    """
    knowledge_base_path = Path(__file__).parent.parent.parent / "knowledge_base" / "planet_fitness.txt"
    try:
        with open(knowledge_base_path, 'r') as file:
            gym_data = file.read()
            return gym_data
    except FileNotFoundError:
        print(f"Error: File not found at {knowledge_base_path}")
        return None

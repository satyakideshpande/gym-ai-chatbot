# Text chunking logic - splits large documents into manageable chunks

import sys
from pathlib import Path
from app.api.chatbot import read_gym_data

def load_and_chunk_data(verbose=True):
    """Load gym data and prepare for chunking.
    
    Args:
        verbose: If True, prints chunks to console
        
    Returns:
        List of text chunks
    """
    gym_data = read_gym_data()

    #Chunking the gym data 
    chunk_size = 500  # characters per chunk
    chunks = []
    for i in range(0, len(gym_data), chunk_size):
        chunks.append(gym_data[i:i+chunk_size])

    if verbose:
        print(f"Data chunked into {len(chunks)} chunks.")
        print("Chunked data looks like this:")
        for idx, chunk in enumerate(chunks, 1):
            print(f"\nChunk {idx}:")
            print(chunk)
            print("-" * 50)
    
    return chunks


if __name__ == "__main__":
    load_and_chunk_data()


# Text chunking logic - splits gym data into meaningful sections

import re
from app.utils.data_loader import read_gym_data


def load_and_chunk_data(verbose=True):
    """
    Load gym data and chunk it by section headings.

    Args:
        verbose: If True, prints chunks to console

    Returns:
        List of text chunks
    """
    gym_data = read_gym_data()

    # Split whenever we encounter a section header
    sections = re.split(r'(?=^===.*?===)', gym_data, flags=re.MULTILINE)

    # Remove empty sections
    chunks = [section.strip() for section in sections if section.strip()]

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
import random

def generate_dna_data(size, length=100):
    """Generates a list of random DNA sequences."""
    bases = ['A', 'T', 'C', 'G']
    return [''.join(random.choices(bases, k=length)) for _ in range(size)]

def calculate_mismatch(seq1, seq2):
    """Counts differences between two DNA strings."""
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

def process_chunk(sequences, target):
    """Processes a chunk of DNA for parallel execution."""
    return [calculate_mismatch(s, target) for s in sequences]

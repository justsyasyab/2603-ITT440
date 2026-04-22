import random

def generate_sequences(count, length=500):
    """Generates a list of random DNA strings."""
    return [''.join(random.choices("ACGT", k=length)) for _ in range(count)]

def dna_alignment_task(target, sequence_batch):
    """Counts mismatches between a target and a list of sequences."""
    results = []
    for seq in sequence_batch:
        score = sum(1 for a, b in zip(target, seq) if a != b)
        results.append(score)
    return results

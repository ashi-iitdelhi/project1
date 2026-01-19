import collections

def get_kmer_counts(sequence, k):
    """
    Analyzes a sequence and returns a dictionary of unique k-mers and their counts.
    
    Args:
        sequence (str): The DNA, RNA, or protein string.
        k (int): The length of the k-mer.
        
    Returns:
        dict: A dictionary with k-mer strings as keys and integers as values.
    """
    # Standardize input to uppercase
    sequence = sequence.upper()
    
    # Initialize an empty dictionary
    kmer_counts = {}
    
    # Check if k is valid for the given sequence
    if k <= 0 or k > len(sequence):
        return kmer_counts

    # Slide the window across the sequence
    # Total windows = N - k + 1
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        
        # Increment count if exists, otherwise initialize to 1
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
            
    return kmer_counts

# --- Execution Block ---
if __name__ == "__main__":
    # Input Data
    test_sequence = "GATTACAGATTACAGATTACA"
    k_value = 3
    
    # Generate counts
    counts = get_kmer_counts(test_sequence, k_value)
    
    # Print Results
    print(f"--- K-mer Analysis (k={k_value}) ---")
    print(f"Sequence: {test_sequence}")
    print(f"Unique k-mers found: {len(counts)}")
    print("-" * 30)
    
    # Sorting by most frequent for better readability
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    
    for kmer, count in sorted_counts.items():
        print(f"{kmer}: {count}")

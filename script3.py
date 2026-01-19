import sys
import os

def count_fasta_records(filepath):
    """
    Parses a multi-FASTA file and counts records.
    Returns: (int, list) -> (count, list_of_headers)
    """
    record_count = 0
    headers = []

    # Check if file exists
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return 0, []

    try:
        with open(filepath, 'r') as fasta_file:
            for line in fasta_file:
                line = line.strip()
                if line.startswith('>'):
                    record_count += 1
                    # Capture the header (removing the '>')
                    headers.append(line[1:])
        
        return record_count, headers

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0, []

# --- Main Execution ---
if __name__ == "__main__":
    # This allows you to pass the filename as an argument: python script3.py seq.mfa
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Default filename if no argument is provided
        input_file = "sequences.mfa"

    # Now the function ALWAYS returns two items, so unpacking won't fail
    count, names = count_fasta_records(input_file)

    print("-" * 40)
    print(f"Results for: {input_file}")
    print(f"Total FASTA records: {count}")
    print("-" * 40)

    if count > 0:
        print("Top Headers:")
        for name in names[:5]: # Show first 5 headers
            print(f"  > {name}")

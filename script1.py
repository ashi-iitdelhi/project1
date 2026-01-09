#!/usr/bin/env python3

import sys

def calculate_fasta_lengths(fasta_file):
    lengths = {}
    seq_id = None

    try:
        with open(fasta_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                if line.startswith(">"):
                    seq_id = line[1:].split()[0]
                    lengths[seq_id] = 0
                else:
                    lengths[seq_id] += len(line)

    except FileNotFoundError:
        print(f"Error: File '{fasta_file}' not found.")
        sys.exit(1)

    return lengths


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    lengths = calculate_fasta_lengths(fasta_file)

    print("Sequence_ID\tLength")
    for seq, length in lengths.items():
        print(f"{seq}\t{length}")

    print(f"\nTotal length: {sum(lengths.values())}")


if __name__ == "__main__":
    main()

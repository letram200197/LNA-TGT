from itertools import combinations
import csv

def generate_lna_combinations_exclude_terminals(sequence, num_lnas):
    """
    Generate DNA sequences with LNA modifications at specific positions, excluding terminals.

    Parameters:
    sequence (str): The original DNA sequence.
    num_lnas (int): The number of LNA modifications to add.

    Returns:
    list: A list of sequences with LNA modifications.
    """
    # Exclude the first and last positions (terminal positions)
    positions = list(range(1, len(sequence) - 1))  # Exclude terminal positions
    comb = combinations(positions, num_lnas)  # Generate combinations of positions for LNA insertion
    
    lna_sequences = []
    for c in comb:
        # Create a mutable copy of the sequence
        new_seq = list(sequence)
        # Add "+" to the positions selected for LNA
        for pos in c:
            new_seq[pos] = "+" + new_seq[pos]
        # Convert the list back to a string and store it
        lna_sequences.append("".join(new_seq))
    
    return lna_sequences

# Example usage:
sequence = "CCCACCAGCGACGCCCGG"
num_lnas = 6  # Specify the number of LNAs to insert
filtered_combinations = generate_lna_combinations_exclude_terminals(sequence, num_lnas)

# Save the results to a CSV file
output_file = "/mnt/data/lna_combinations_6_excluding_terminals.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sequence"])  # Write the header
    for seq in filtered_combinations:
        writer.writerow([seq])

def main():
    print("If you would like to quit, type 'quit'")
    dna_sequence = input("Provide a DNA sequence: ").upper()

    while dna_sequence != "QUIT":
        try:
            identified_genes = find_sequence(dna_sequence)
        except:
            print("DNA sequence you provided contains invalid characters.")
        else:
            if len(identified_genes) == 0:
                print("No potential genes were identified.")
            else:
                print("Identified potential genes within a genome: ")
                print(identified_genes)
                print()

        dna_sequence = input("Provide a DNA sequence: ").upper()


def find_sequence(dna_sequence: str):
    """
    Identifies potential genes within a given DNA sequence.
    A gene is defined as a sequence of codons (each codon being a sequence of three bases),
    beginning with the start codon 'ATG' and ending with one of the stop codons 'TAG', 'TAA',
    or 'TGA'. The identified gene must have a length of min 3 codons and length that is a multiple of three
    and must not contain any intervening stop codons.

    :return: A list of strings, each representing a detected gene sequence from a start codon to a stop codon.
    """
    allowed_chars = {"A", "T", "G"}

    for char in dna_sequence:
        if char not in allowed_chars:
            raise ValueError("Invalid DNA sequence")

    start_codon = {"ATG"}
    end_codon = {"TAG", "TGA", "TAA"}

    # Initialize the list to store all potential gene sequences
    list_det_seq = []
    detect_seq = ""

    for i in range(len(dna_sequence) - 8):
        # Steps 1 codon as 1 codon's length is 3
        if dna_sequence[i:i + 3] in start_codon:
            detect_seq += dna_sequence[i:i + 3]

            # Once the start codon is identified, the program tries to find the stop codon
            j = i
            while dna_sequence[j + 3:j + 6] not in end_codon and j < len(dna_sequence) - 3:
                detect_seq += dna_sequence[j + 3:j + 6]
                j += 3

            # Ensures that j does not exceed sequence's length
            if j < len(dna_sequence) - 3:
                # Adds last codon
                if dna_sequence[j + 3:j + 6] in end_codon:
                    detect_seq += dna_sequence[j + 3:j + 6]
            else:
                # Assigns "" to detect_seq as the stop codon was not found
                detect_seq = ""

            # Adds to the list the detected sequence
            if detect_seq != "" and len(detect_seq) != 6:
                list_det_seq.append(detect_seq)

            detect_seq = ""

    # The sequence with length 6 does not exist
    if len(detect_seq) == 6:
        detect_seq = ""

    return list_det_seq


if __name__ == '__main__':
    main()


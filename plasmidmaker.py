import sys

def create_plasmid():
    # 1. Essential Genes from the paper (IncQ/RSF1010 example)
    # The paper highlights RepA (helicase), RepB (primase), and RepC (initiator)
    rep_genes = "ATGC_RepA_Helicase_RepB_Primase_RepC_Initiator_OriV"

    # 2. Read Input.Fa
    try:
        with open('Input.Fa', 'r') as f:
            dna_input = "".join([line.strip() for line in f if not line.startswith(">")])
    except FileNotFoundError:
        print("Error: Input.Fa not found")
        return

    # 3. Read Design.txt
    design_elements = ""
    try:
        with open('Design.txt', 'r') as f:
            for line in f:
                if ',' in line:
                    parts = line.strip().split(',')
                    design_elements += f"_{parts[1].strip()}_"
    except FileNotFoundError:
        print("Error: Design.txt not found")
        return

    # 4. Assemble and Save
    full_sequence = rep_genes + dna_input + design_elements
    with open('Output.Fa', 'w') as f:
        f.write(">Universal_Plasmid_Output\n")
        f.write(full_sequence)
    
    print("Process Complete. Output.Fa has been created.")

if __name__ == "__main__":
    create_plasmid()

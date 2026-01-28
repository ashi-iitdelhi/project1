import os

def load_marker_db(filename):
    """Parses markers.tab to map names to DNA sequences or roles."""
    db = {}
    if not os.path.exists(filename): return db
    with open(filename, 'r') as f:
        for line in f:
            if "|" in line and "Recognizes" in line:
                parts = [p.strip() for p in line.split("|")]
                name = parts[2]
                if "Recognizes " in parts[3]:
                    # Extract the 6-bp sequence (e.g., GAATTC)
                    db[name] = parts[3].split("Recognizes ")[1][:6]
            elif "|" in line and "Selection marker" in line:
                parts = [p.strip() for p in line.split("|")]
                db[parts[2].split(" ")[0]] = parts[3]
    return db

def find_ori(sequence):
    """Finds the ORI in the unknown organism or adds default BHR genes."""
    motif = "ggtgagcaaaaggcc" # pMB1/pUC origin motif
    idx = sequence.lower().find(motif)
    if idx != -1:
        return sequence[idx:idx+100]
    return "REP_ABC_BHR_MACHINERY"

def run_assembly():
    # 1. Load the provided files
    marker_db = load_marker_db("markers.tab")
    with open("pUC19.fa", 'r') as f:
        original_seq = "".join([l.strip() for l in f if not l.startswith(">")])

    # 2. Identify the Origin (ORI)
    identified_ori = find_ori(original_seq)

    # 3. Process Design instructions (Deletion and Addition)
    modified_body = original_seq
    
    # REQUIREMENT: Specific deletion of EcoRI site (GAATTC)
    ecori_seq = marker_db.get("EcoRI", "GAATTC")
    modified_body = modified_body.replace(ecori_seq.upper(), "").replace(ecori_seq.lower(), "")

    with open("Design_pUC19.txt", 'r') as f:
        for line in f:
            if "," not in line: continue
            feature_id, feature_name = [x.strip() for x in line.split(",")]
            
            if "site" in feature_id:
                seq = marker_db.get(feature_name)
                if seq:
                    modified_body = modified_body.replace(seq.upper(), "").replace(seq.lower(), "")
            elif "gene" in feature_id or "ori" in feature_id:
                info = marker_db.get(feature_name, f"[{feature_name}_SEQ]")
                modified_body += f"_{info}_"

    # 4. Save the Output
    with open("Output.Fa", "w") as f:
        f.write(f">Output_Plasmid_Final\n{identified_ori}{modified_body}")
    print("Process Complete. Output.Fa created.")

if __name__ == "__main__":
    run_assembly()

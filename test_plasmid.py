import os

def verify():
    print("--- Running Automated Tests ---")
    os.system("python3 plasmidmaker.py")
    
    if os.path.exists("Output.Fa"):
        with open("Output.Fa", "r") as f:
            content = f.read().upper()
            # Test: Is EcoRI (GAATTC) gone?
            if "GAATTC" not in content:
                print("PASS: EcoRI site successfully deleted.")
            else:
                print("FAIL: EcoRI site is still in the plasmid.")
    else:
        print("FAIL: Output.Fa was not found.")

if __name__ == "__main__":
    verify()

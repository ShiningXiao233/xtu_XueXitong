import sys

if __name__ == "__main__":
    fin = sys.argv[1]
    fou = sys.argv[2]
    with open(fin, "r", encoding="utf-8") as f:
        in_txt = f.read()
    
    with open(fou, "a", encoding="utf-8") as f:
        f.write(in_txt)
        
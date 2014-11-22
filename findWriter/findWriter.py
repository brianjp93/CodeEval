import sys

with open(sys.argv[1], "r") as f:
    for line in f:
        if line.strip() == "":
            pass
        else:
            parts = line.strip().split("|")
            indices = parts[1].strip().split()
            coded = parts[0]
            decoded = ""
            for index in indices:
                decoded += coded[int(index)-1]
            print(decoded)
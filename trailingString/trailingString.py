import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        parts = line.strip().split(",")
        sentence = parts[0][::-1]
        end = parts[1][::-1]
        if sentence.startswith(end):
            print(1)
        else:
            print(0)
import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip().split(",")
        n1, n2 = int(line[0]), int(line[1])
        print(n1 - (n1//n2)*n2)
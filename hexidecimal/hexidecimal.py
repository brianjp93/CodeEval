import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        hexi = line.strip()
        i = int(hexi, 16)
        print(i)
import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        for i in range(len(line)):
            if int(line[i]) != line.count(str(i)):
                print(0)
                break
            elif i == len(line) - 1:
                print(1)

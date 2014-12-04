import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip().split()
        count = 1
        output = ""
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                count += 1
            else:
                output += str(count) + " " + str(line[i]) + " "
                count = 1
        output += str(count) + " " + str(line[len(line) - 1]) + " "
        print(output.strip())
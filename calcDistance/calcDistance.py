import sys
import math

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip().strip("(").strip(")").split(" ")
        line = list(map(lambda x: x.strip(",").strip("(").strip(")"), line))
        dif1 = int(line[0]) - int(line[2])
        dif2 = int(line[1]) - int(line[3])
        dist = math.sqrt(dif1**2 + dif2**2)
        print(int(dist))
import sys

with open(sys.argv[1], 'r') as f:
	for line in f:
		multplied = ""
		line = line.rstrip().split(" | ")
		l1, l2 = line[0].split(), line[1].split()
		for i in range(len(l1)):
			multplied += str(int(l1[i]) * int(l2[i])) + " "
		print(multplied.rstrip())
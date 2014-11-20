import sys
with open(sys.argv[1], 'r') as f:
	for line in f:
		output = ""
		nums = line.strip().split()
		for i in range(0, len(nums), 2):
			output += nums[::-1][i] + " "
		print(output.strip())
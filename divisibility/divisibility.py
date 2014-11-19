import sys
filename = sys.argv[1]

with open(filename, 'r') as f:
	for line in f:
		splitLine = line.split()
		x = int(splitLine[0])
		y = int(splitLine[1])
		n = int(splitLine[2])
		output = ""
		for i in range(n):
			i += 1
			if i%x == 0 and i%y == 0:
				output += "FB"
			elif i%x == 0:
				output += "F"
			elif i%y == 0:
				output += "B"
			else:
				output += str(i)
			output += " "
		output = output.strip()
		print(output)
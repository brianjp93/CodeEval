largest = 0
for i in range(1, 1001):
	blah = False
	if str(i) == str(i)[::-1]:
		for j in range(2, i//2 + 1):
			if i%j == 0:
				break
			elif j == i//2:
				largest = i
print(largest)
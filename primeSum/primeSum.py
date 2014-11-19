summed = 2
num = 0
num_primes = 1
while num_primes < 1000:
	for j in range(2, num//2 + 2):
		if num%j == 0:
			# print(j)
			break
		elif j == num//2 + 1:
			# print(num)
			summed += num
			num_primes += 1
	num += 1
print(summed)
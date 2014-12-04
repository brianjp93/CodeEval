def is_prime(n):
    first = [1,2,3,5,7]
    if n in first:
        return True
    # divisible by 2
    if n % 2 == 0:
        return False
    # divisible by 3
    total = 0
    for c in str(n):
        total += int(c)
    if total % 3 == 0:
        return False
    # divisible by 5
    if int(str(n)[-1]) == 5 or int(str(n)[-1]) == 0:
        return False
    # divisible by 9
    total = 0
    for c in str(n):
        total += int(c)
    if total % 9 == 0:
        return False
    # else must brute force
    for i in range(1, n // 2 + 1, 2):
        for j in range(i, n // 2 + 1, 2):
            if i * j == n:
                return False
    return True

for i in range(15440, 20000):
    if is_prime(i):
        f = open("primeList.txt", 'a')
        f.write(str(i) + ", ")
    else:
        pass

f.close()
#
# with open("primes.txt", "r") as f:
#     for line in f:
#         line = line.strip().split()
#         with open("primeList.txt", "a") as out:
#             out.write(", ".join(line))
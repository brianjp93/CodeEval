import sys


def int_pals(begin, end):
    total = 0
    num_int_pals = 0
    for i in range(begin, end + 1):
        num = str(i)
        if num == num[::-1]:
            total += 1
    if total == 1:
        return 1
    elif total % 2 != 0:
        adding = 2
        while adding <= total:
            num_int_pals += adding
            adding += 2
    else:
        adding = 1
        while adding <= total:
            num_int_pals += adding
            adding += 2
    return num_int_pals

with open(sys.argv[1], 'r') as f:
    for line in f:
        numbers = line.strip().split()
        num_pals = int_pals(int(numbers[0]), int(numbers[1]))
        print(num_pals)
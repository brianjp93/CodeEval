import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        num = line.strip()
        total = 0
        digits = len(num)
        for i in num:
            total += int(i)**digits
        if total == int(num):
            print("True")
        else:
            print("False")
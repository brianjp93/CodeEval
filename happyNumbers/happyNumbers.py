import sys

happyNums = (1, 7, 10)
notHappyNums = (2, 3, 4, 5, 6, 8, 9)

with open(sys.argv[1], 'r') as f:
    for line in f:
        num = int(line.strip())
        if num == 1:
            print(1)
        while num != 1:
            if num in happyNums:
                print(1)
                break
            elif num in notHappyNums:
                print(0)
                break
            else:
                num = str(num)
                total = 0
                for i in num:
                    total += int(i) ** 2
                num = total
                if num == 1:
                    print(1)

import sys
import math

def findDoubleSquares(n):
    if n == 0:
        return 1
    else:
        numDoubleSquares = 0
        for i in range(int(math.sqrt(n) + 1)):
            square1 = i ** 2
            num2 = n - square1
            if math.sqrt(num2) % 1 == 0:
                numDoubleSquares += 1
        if numDoubleSquares % 2 == 0:
            numDoubleSquares /= 2
        else:
            numDoubleSquares = (numDoubleSquares - 1)/2
        return int(numDoubleSquares)

with open(sys.argv[1], 'r') as f:
    for i, n in enumerate(f):
        if i == 0:
            pass
        else:
            n = int(n.strip())
            numDoubles = findDoubleSquares(n)
            print(numDoubles)
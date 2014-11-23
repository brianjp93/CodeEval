import sys
from datetime import datetime

def computeYears(dates):
    # sort dates
    dates = sorted(dates, key = lambda x: x[0])
    pass

with open(sys.argv[1], 'r') as f:
    for line in f:
        dates = []
        line = line.strip().split("; ")
        for double in line:
            double = double.split("-")
            first = double[0]
            second = double[1]
            first = datetime.strptime(first, "%b %Y")
            second = datetime.strptime(second, "%b %Y")
            dates.append([first, second])
        print(computeYears(dates))
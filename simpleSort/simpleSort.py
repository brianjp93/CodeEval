import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        nums = list(map(float, line.strip().split()))
        sort_nums = list(map("{0:.3f}".format, sorted(nums)))
        print(" ".join(sort_nums))

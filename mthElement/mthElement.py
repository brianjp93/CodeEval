import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        whole = line.strip().split()
        mth = int(whole[-1])
        if mth >= len(whole):
            pass
        else:
            rest = whole[::-1]
            print(rest[mth])
import sys
from string import ascii_lowercase

with open(sys.argv[1], 'r') as f:
    for line in f:
        letters = set()
        for l in ascii_lowercase:
            letters.add(l)
        line = line.strip()
        for l in line:
            if l.lower() in letters:
                letters.remove(l.lower())
        letterList = sorted(list(letters))
        if len(letterList) == 0:
            print("NULL")
        else:
            print("".join(letterList))
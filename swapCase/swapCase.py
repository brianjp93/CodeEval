import sys
import string

def switch(l):
    if l in string.ascii_letters:
        if l == l.upper():
            return l.lower()
        else:
            return l.upper()
    else:
        return l

with open(sys.argv[1], 'r') as f:
    for line in f:
        array = []
        line = line.strip()
        for l in line:
            array.append(l)
        swapped = list(map(switch, array))
        print(''.join(swapped))
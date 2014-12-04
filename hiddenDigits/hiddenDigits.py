import sys

firstLetters = 'abcdefghij'

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        output = ""
        for ch in line:
            if ch in firstLetters:
                output += str(firstLetters.index(ch))
            elif ch.isdigit():
                output += ch
        if output == "":
            print("NONE")
        else:
            print(output)
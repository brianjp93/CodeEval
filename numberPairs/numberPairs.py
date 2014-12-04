import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        if line == "":
            pass
        else:
            line = line.strip().split(";")
            nums = list(map(int, line[0].split(",")))
            ans = int(line[1])
            numSet = {x for x in nums}
            output = ""
            for n in nums:
                if ans - n != n and ans - n in numSet and str(n) not in output:
                    output += str(n) + "," + str(ans - n) + ";"
            if output == "":
                print("NULL")
            else:
                print(output.strip(";"))

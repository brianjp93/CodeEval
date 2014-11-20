import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        sep = line.strip().split(";")
        num1, num2 = sep[0], sep[1]
        set1 = set(num1.split(","))
        set2 = set(num2.split(","))
        inter = list(set1 & set2)
        sorted_inter = list(map(str, sorted(list(map(int, inter)))))
        print(",".join(sorted_inter).strip(","))
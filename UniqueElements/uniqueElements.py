import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        unique = set()
        nums = list(map(int, line.strip().split(",")))
        for num in nums:
            if num not in unique:
                unique.add(num)
        output = ",".join(list(map(str, (sorted(list(unique))))))
        print(output.strip(",").strip())
import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        unique = set()
        unique_ordered = []
        nums = line.strip().split(",")
        for num in nums:
            if num not in unique:
                unique_ordered.append(num)
                unique.update(num)
        output = ",".join(unique_ordered)
        print(output.strip(",").strip())
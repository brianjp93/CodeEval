import sys
import string

with open(sys.argv[1], 'r') as f:
    for line in f:
        alpha_points = {}
        total = 0
        points = 26
        line = line.strip().lower()
        for l in line:
            if l in string.ascii_lowercase:
                if l in alpha_points:
                    alpha_points[l] += 1
                else:
                    alpha_points[l] = 1
        alpha_sorted = sorted(alpha_points, key=lambda x: alpha_points[x])
        for l in reversed(alpha_sorted):
            total += alpha_points[l]*points
            points -= 1
        print(total)
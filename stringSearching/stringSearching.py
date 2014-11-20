import sys


def check_vals(in_string, vals):
    found = []
    val_num = 0
    j = 0
    for i in range(len(in_string)):
        if in_string[i] == vals[val_num][j]:
            j += 1
            if j == len(vals[val_num]):
                found.append(vals[val_num])
                j = 0
                val_num += 1
                if val_num == len(vals):
                    break
    if len(found) == len(vals):
        return True
    else:
        return False

with open(sys.argv[1], 'r') as f:
    for line in f:
        full = line.strip().split(",")
        in_string = full[0]
        to_check = full[1].split("*")
        if check_vals(in_string, to_check):
            print("true")
        else:
            print("false")
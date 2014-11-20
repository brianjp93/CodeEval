import sys


def check_vals(in_string, vals):
    pass

with open('test.txt', 'r') as f:
    for line in f:
        full = line.strip().split(",")
        in_string = full[0]
        to_check = full[1].split("*")
        if check_vals(in_string, to_check):
            print("true")
        else:
            print("false")
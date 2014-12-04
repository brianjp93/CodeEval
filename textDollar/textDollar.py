import sys

tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] + teens
magnitudes = ["", "One", "Ten", "Hundred", "Thousand", "Million", "Billion"]
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        mag = len(line)
        output = ""
        for i, n in enumerate(line):
            if mag >= 3 and (mag - i) % 3 == 1:
                output += ones[int(n)]
                output += magnitudes[mag]
            elif mag >= 3 and (mag - i) % 3 == 0:
                output += ones[int(n)]
                if int(n) != 0:
                    output += "Hundred"
            elif mag >= 3 and (mag - i) % 3 == 2:
                if int(n) >= 2:
                    output += tens[int(n)]
import sys

def validate(email):
	test = email.split("@")
	if len(email) <= 4:
		return "false"
	elif " " in email:
		return "false"
	elif "@" not in email:
		return "false"
	elif not email.endswith(".com"):
		return "false"
	elif len(test[1]) <= 4 or len(test[0]) == 0:
		return "false"
	else:
		return "true"

with open(sys.argv[1], 'r') as f:
	for line in f:
		if line == "":
			pass
		else:
			line = line.rstrip()
			print(validate(line))
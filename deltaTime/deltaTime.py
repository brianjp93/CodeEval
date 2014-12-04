import sys
from datetime import datetime, timedelta

with open(sys.argv[1], 'r') as f:
	for line in f:
		line = line.rstrip()
		times = line.split()
		time1, time2 = times[0], times[1]
		time1 = datetime.strptime(time1, "%H:%M:%S")
		time2 = datetime.strptime(time2, "%H:%M:%S")
		if time1 > time2:
			output = time1 - timedelta(hours = time2.hour, minutes = time2.minute, seconds = time2.second)
			output = datetime.strftime(output, "%H:%M:%S")
			print(output)
		else:
			output = time2 - timedelta(hours = time1.hour, minutes = time1.minute, seconds = time1.second)
			output = datetime.strftime(output, "%H:%M:%S")
			print(output)
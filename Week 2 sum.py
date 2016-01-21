import re

sum = 0

dataFile = open('regex_sum_232580.txt')
for line in dataFile:
	y = re.findall('[0-9]+', line)
	for num in y:
		sum += int(num)
print sum	
import urllib, json, re

url = raw_input('Enter location: ')

openFile = urllib.urlopen(url)
readFile = openFile.read()
result = json.loads(str(readFile))
numList = []

print 'Retrieving ' + url
count = 0
sum = 0

for line in result['comments']:
	count += 1
	numList.append(line.get('count', None))

for num in numList:
	sum += int(num)
	
print 'Retrieved ' + str(len(readFile)) + ' characters'
print 'Count: ' + str(count)
print 'Sum: ' + str(sum)
import xml.etree.ElementTree as ET
import urllib

url = raw_input('Enter URL: ')

result = []
sum = 0

rec = urllib.urlopen(url)
read = rec.read()
tree = ET.fromstring(read)

results = tree.findall('comments/comment')

for line in results:
	result.append(line.find('count').text)
	
for num in result:
	sum += int(num)
	
print sum
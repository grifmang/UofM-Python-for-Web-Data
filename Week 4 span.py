import urllib
from BeautifulSoup import *
import re

sum = 0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags:
	tag = str(tag)
	y = re.findall('[0-9]+', tag)
	for num in y:
		sum += int(num)
print sum

import urllib
from BeautifulSoup import *

def build_soup(url):
	site = urllib.urlopen(url).read()
	soup = BeautifulSoup(site)
	tags = soup('a')
	return tags
	
def get_site(url):
	results = []
	tags = build_soup(url)
	for tag in tags:
		results.append(tag.get('href', None))
	return results

count = 0
url = str(raw_input('Enter URL: '))
counter = int(raw_input('Enter Count: '))
pos = raw_input('Enter Position: ')

while count < counter:
	site = get_site(url)
	next = site[int(pos) - 1]
	print 'Retrieving: ' + str(next)
	url = next
	count += 1
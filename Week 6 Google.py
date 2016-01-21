import urllib, json

constantUrl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	location = raw_input('Enter location: ')
	url = constantUrl + urllib.urlencode({'sensor':'false', 'address': location})
	print 'Retrieving', url
	openFile = urllib.urlopen(url)
	readFile = openFile.read()
	results = json.loads(readFile)
	print 'Retrieved ' + str(len(readFile))
	
	for line in results['results']:
		placeID = line.get('place_id', None)
		if line.keys() == 'place_id':
			placeID = line
	
	print 'Place ID: ' + str(placeID)
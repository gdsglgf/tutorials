try:
	from urllib.request import Request, urlopen, urlretrieve  # Python 3
except:
	from urllib2 import Request, urlopen  # Python 2
	from urllib import urlretrieve

def get_content(url):
	headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
	req = urllib2.Request(url, headers=headers)
	socket = urllib2.urlopen(req)
	content = socket.read()
	socket.close()

	return content


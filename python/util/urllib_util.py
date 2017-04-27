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


#! /usr/bin/env python2
import urllib 
import urllib2 
url = 'http://www.pythontab.com' 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
  
values = {'name' : 'Michael Foord', 
          'location' : 'pythontab', 
          'language' : 'Python' } 
headers = { 'User-Agent' : user_agent } 
data = urllib.urlencode(values) 
req = urllib2.Request(url, data, headers) 
response = urllib2.urlopen(req) 
the_page = response.read()



#! /usr/bin/env python3
import urllib.parse
import urllib.request

url = 'http://localhost/login.php'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
'act' : 'login',
'login[id]' : '123456',
'login[password]' : '123456'
}
headers = { 'User-Agent' : user_agent }

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
the_page = response.read()

print(the_page.decode("utf8"))
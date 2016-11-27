import sys
version = sys.version_info[0]
if version == 2:
	from urllib2 import Request, urlopen  # Python 2
	from urllib import urlretrieve
else:
	from urllib.request import Request, urlopen, urlretrieve  # Python 3


## python 3 version
# import urllib.request as request
# url = 'http://www.oschina.net'
# headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
# opener = request.build_opener()
# opener.addheaders = [ headers ]
# origin_bytes = opener.open( url ).read()
# origin_string = origin_bytes.decode( 'utf-8' )
# print(origin_string)


url = 'http://yuedu.fm/'
headers = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
req = Request(url, headers=headers)
res = urlopen(req).read().decode('utf-8')
print(type(res))
print(res)
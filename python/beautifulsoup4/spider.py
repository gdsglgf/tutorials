from datetime import datetime
import os
import sys
import socket
timeout = 20
socket.setdefaulttimeout(timeout)
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

def create_filename():
	now = datetime.now().strftime('%Y%m%d%H%M%S')
	filename = '%s.html' %(now)
	return filename

def show_html(url):
	headers = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
	req = Request(url, headers=headers)
	try:
		request = urlopen(req)
		html = request.read().decode('utf-8')
		request.close()
		print(type(html))
		print(html)
	except Exception, e:
		print(e)
		

def report(blockstep, blocksize, totalsize):
	'''Call back function
	@blockstep: number of block downloaded
	@blocksize: bytes per block
	@totalsize: bytes of file
	'''
	if totalsize == 0:
		return
	downloaded = blockstep * blocksize
	percent = 100.0 * downloaded / totalsize
	if percent > 100:
		percent = 100
	downloaded = downloaded if downloaded < totalsize else totalsize
	os.write(1, "\r%d/%d, %.2f%%..." %(downloaded, totalsize, percent))
	sys.stdout.flush()

def download(url, filename):
	try:
		urlretrieve(url, filename, report)
		print('\ndownlaoded file:%s' %(filename))
	except Exception, e:
		print(e)

def download_large(url, filename=None):
	file_name = filename if filename else url.split('/')[-1]
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
	# headers = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
	request = Request(url, headers=headers)
	response = urlopen(request)

	# response = urlopen(url)

	f = open(file_name, 'wb')
	meta = response.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print("Downloading: %s Bytes: %s" % (file_name, file_size))

	file_size_dl = 0
	block_sz = 8192
	while True:
		buf = response.read(block_sz)
		if not buf:
			break

		file_size_dl += len(buf)
		f.write(buf)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		os.write(1, "\r%s" %(status))
		sys.stdout.flush()

	f.close()
	request.close()

if __name__ == '__main__':
	params = sys.argv
	num_param = len(params)
	if num_param < 3 or not params[1] in ['-d', '-s', '-ds', '-l']:
		msg = '''Usage:
python spider.py -s url # show html in console
python spider.py -d url [filename] # download html in filename
python spider.py -ds url [filename] # show and download
python spider.py -l url # download large file
'''
		print(msg)
	else:
		cmd = params[1]
		url = params[2]
		filename = create_filename() if num_param == 3 else params[3]
		if cmd == '-s':
			show_html(url)
		elif cmd == '-d':
			download(url, filename)
		elif cmd == '-ds':
			show_html(url)
			download(url, filename)
		else:
			download_large(url, filename)
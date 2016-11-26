# -*- coding: utf-8 -*-
import os
import sys
try:
	from urllib.request import Request, urlopen, urlretrieve  # Python 3
except:
	from urllib2 import Request, urlopen  # Python 2
	from urllib import urlretrieve
from PIL import Image

# header = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
# req = Request(url, header=header)

def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)
		return True
	return False

def callbackfunc(blockstep, blocksize, totalsize):
	'''回调函数
	@blockstep: 已经下载的数据块
	@blocksize: 数据块的大小
	@totalsize: 远程文件的大小
	'''
	if totalsize == 0:
		return
	percent = 100.0 * blockstep * blocksize / totalsize
	if percent > 100:
		percent = 100
	print "%.2f%%"% percent

def show_counter(counter):
	for key, value in counter.items():
		print key, value

def is_valid(path):
	status = True
	try:
		img = Image.open(path)
	except:
		print 'cannot open file: %s' %(path)
		status = False
	return status

def download(url, path):
	if not os.path.exists(path):
		print 'download file %s, url: %s' %(path, url)
		urlretrieve(url, path, callbackfunc)
	elif not is_valid(path):
		if os.path.exists(path):
			os.remove(path)
			print 'remove file %s' %(path)
		print 'download file %s, url: %s' %(path, url)
		urlretrieve(url, path, callbackfunc)

def maybe_download(work_directory, csv, url_index, label_index):
	if not mkdir(work_directory):
		print 'The directory is exist: %s' %work_directory
		# return

	counter = {}
	step = 0
	with open(csv, 'r') as f:
		next(f)		# skip csv header title
		for line in f:
			row = line.rstrip('\n').split(',')
			url = row[url_index]
			label = row[label_index]

			count = counter.get(label, 0)
			counter[label] = count + 1
			filename = '%s_%d.jpg' %(label, count)
			path = os.path.join(work_directory, filename)
			# print step, path
			step += 1

			download(url, path)

	show_counter(counter)

def download_data(work_directory):
	# seq,image_url,wk_content_policy_cd
	csv = 'image_dataset_label.csv'
	maybe_download(work_directory, csv, 1, 2)

def download_thumbnail(work_directory):
	# seq, image_url, image_thumbnail, wk_content_policy_cd
	csv = 'image_dataset_label_thumbnail.csv'
	maybe_download(work_directory, csv, 2, 3)

def data_count(filename):
	print filename
	counter = {}
	with open(filename) as f:
		next(f)
		for line in f:
			row = line.rstrip('\n').split(',')
			label = row[-1]
			count = counter.get(label, 0)
			counter[label] = count + 1

	show_counter(counter)

# PP05 4095
# PP15 19025
# PP01 10747
# PP02 16101
# PP03 32
def show_data_count():
	f1 = 'image_dataset_label.csv'
	f2 = 'image_dataset_label_thumbnail.csv'
	data_count(f1)
	data_count(f2)

def file_count(dirs):
	for dest in dirs:
		filenames = [f for f in os.listdir(dest) if f.endswith('.jpg')]
		print '%s has %d file(s)' %(dest, len(filenames))

		labels = ['PP01', 'PP02', 'PP03', 'PP05', 'PP15']
		total = 0
		for label in labels:
			fs = [f for f in os.listdir(dest) if f.startswith(label)]
			count = len(fs)
			total += count
			print '%s has %d file(s)' %(label, count)

		print '%s has %d file(s)' %(dest, total)

def findMin(dirs):
	for dest in dirs:
		images = [f for f in os.listdir(dest) if f.endswith('.jpg')]
		minH, minW = 65536, 65536
		fpH, fpW = '', ''
		step = 0
		for f in images:
			if not is_valid(os.path.join(dest, f)):
				continue
			h, w = img.size
			
			if minH > h:
				minH = h
				fpH = f

			if minW > w:
				minW = w
				fpW = f

			if step % 100 == 0:
				print f, minH, minW
			step += 1

		print minH, minW
		print fpH, fpW

def remove_invalid_data(dirs):
	for dest in dirs:
		images = [f for f in os.listdir(dest) if f.endswith('.jpg')]
		remove_count = 0
		total = len(images)
		for i, f in enumerate(images, start=1):
			try:
				path = os.path.join(dest, f)
				img = Image.open(path)
			except:
				if os.path.exists(path):
					os.remove(path)
					remove_count += 1
					print 'remove file: %s' %(f)
				continue
			os.write(1, '\r%d/%d %s' %(i, total, f))
			sys.stdout.flush()
		print '\n%s, total %d files, remove %d files' %(dest, len(images), remove_count)

def view_image_size(dirs):
	for dest in dirs:
		images = [f for f in os.listdir(dest) if f.endswith('.jpg')]
		for f in images:
			try:
				img = Image.open(os.path.join(dest, f))
				h, w = img.size
				print f, h, w
			except:
				print 'cannot open file: %s' %(f)
				continue

if __name__ == '__main__':
	data_dir = 'data/'
	thumbnail_dir = 'thumbnail/'

	dirs = [data_dir, thumbnail_dir]

	command = ''
	if len(sys.argv) >= 2:
		command = sys.argv[1]

	if command == '1':
		download_data(data_dir)
	elif command == '2':
		download_thumbnail(thumbnail_dir)
	elif command == '3':
		if len(sys.argv) >= 3:
			dirs = sys.argv[2:]
		remove_invalid_data(dirs)
	elif command == '4':
		view_image_size(dirs)
	elif command == '5':
		findMin(dirs)
	else:
		show_data_count()
		file_count(dirs)
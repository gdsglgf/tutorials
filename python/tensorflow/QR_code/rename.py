import os
from PIL import Image

data_dir = 'origin'
common = 'image'
filenames = [f for f in os.listdir(data_dir) if f.startswith(common)]

labels = ['0', '1']

# print len(filenames)

def rename():
	counter = 0
	for f in filenames:
		new = os.path.join(data_dir, '%s%d.png' %(common, counter))
		os.rename(os.path.join(data_dir, f), new)

		counter += 1
		print 'rename %s -> %s' %(f, new)

def creatHtml():
	for i in range(len(filenames)):
		print '		<img src="image%d.png"><input type="checkbox" class="choose">%d' %(i, i)

def rename2():
	for i in range(len(filenames)):
		old = 'images(%d)' %(i)
		new = 'image%d.png' %(i)
		os.rename(old, new)

def filename(i):
	return 'image%s.png' %(i)

def loadDataset():
	data = {}
	for label in labels:
		data[label] = []

	with open('dataset.txt') as f:
		for line in f:
			line = line.rstrip('\n')
			id, flag = line.split(' ')
			data[flag].append(id)

	print len(data['0']), len(data['1'])		# 158 222
	return data

def classifyImage():
	data = loadDataset()

	for label in labels:
		for i in data[label]:
			if not os.path.exists(label):
				os.mkdir(label)

			old = filename(i)
			new = '%s/%s' %(label, old)
			os.rename(old, new)

def viewImage():
	data = loadDataset()
	for label in labels:
		for i in data[label]:
			f = os.path.join(label, filename(i))
			img = Image.open(f)
			print f, img.size, img.mode, img.format

if __name__ == '__main__':
	# creatHtml()
	viewImage()

import os
from PIL import Image

def listFiles(dest, suffix):
	return [f for f in os.listdir(dest) if f.endswith(suffix)]

def mkdir(dest):
	if not os.path.exists(dest):
		os.mkdir(dest)

def viewImage(dest, suffix='.jpg'):
	if not os.path.exists(dest):
		print 'Not exist directory: %s' %(dest)
		return

	images = listFiles(dest, suffix)

	for f in images:
		img = Image.open(os.path.join(dest, f))
		print f, img.size, img.mode, img.format

def convert(src, suffix='.png'):
	images = listFiles(dest, suffix)

	if len(images) == 0:
		return

	dest = '%s_formated' %(src)
	mkdir(dest)

	for f in images:
		img = Image.open(os.path.join(src, f))
		fp = os.path.join(dest, f.split('.')[0] + '.jpg')
		img.convert('RGB').save(fp)
		print fp

	viewImage(dest)

def findMin(dest, suffix='.jpg'):
	images = listFiles(dest, suffix)
	minH, minW = 65536, 65536
	fpH, fpW = '', ''
	for f in images:
		img = Image.open(os.path.join(dest, f))
		size = img.size
		
		if minH > size[0]:
			minH = size[0]
			fpH = f

		if minW > size[1]:
			minW = size[1]
			fpW = f

	print minH, minW
	print fpH, fpW

def resize(src, suffix='.jpg', size=(128, 128)):
	images = listFiles(src, suffix)

	if len(images) == 0:
		return

	dest = '%s_resize' %(src)
	mkdir(dest)

	for f in images:
		img = Image.open(os.path.join(src, f))
		fp = os.path.join(dest, f)
		img.resize(size).save(fp)

	viewImage(dest)

def toBlackAndWhite(src, suffix='.jpg', size=(128, 128)):
	images = listFiles(src, suffix)

	if len(images) == 0:
		return

	dest = '%s_bw' %(src)
	mkdir(dest)

	for f in images:
		img = Image.open(os.path.join(src, f))
		fp = os.path.join(dest, f)
		img.resize(size).convert('1').save(fp)

	viewImage(dest)


if __name__ == '__main__':
	# findMin('0_formated')
	# findMin('1_formated')
	# resize('0_formated')
	# resize('1_formated')

	toBlackAndWhite('0_formated_resize')
	toBlackAndWhite('1_formated_resize')
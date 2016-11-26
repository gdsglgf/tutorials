#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def addSalt(path):
	img = np.array(Image.open(path))

	#随机生成5000个椒盐
	rows,cols,dims = img.shape
	print img.shape
	print rows, cols, dims
	for i in range(5000):
		x = np.random.randint(0,rows)
		y = np.random.randint(0,cols)
		img[x,y,:] = 255
		
	show2(img)

def info(img):
	print '-------image-------'
	print type(img)
	print img.size  #图片的尺寸
	print img.mode  #图片的模式
	print img.format  #图片的格式

def arrayInfo(data):
	print '--------numpy.ndarray-------'
	print data
	print data.shape
	print data.dtype
	print data.size  #图片的尺寸
	print type(data)

def showZeroOneImage(path):
	img = np.array(Image.open(path).convert('1'))
	# rows, cols = img.shape
	# print img.shape
	# img = img.reshape(rows * cols)
	# img = np.array([1 if i else 0 for i in img])
	# img = img.reshape(rows, cols)
	print img

	show2(img)

def toZeroOne(img):
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			if (img[i, j] <= 128):
				img[i, j] = 0
			else:
				img[i, j] = 1
	return img

def showBlackWhiteImage(path):
	img = np.array(Image.open(path).convert('L'))
	print img.shape
	print img
	show2(img)

	img = toZeroOne(img)
	show2(img)

def showDiff(path):
	plt.figure(path)
	plt.subplot(2, 2, 1)
	plt.title('1')
	plt.imshow(np.array(Image.open(path).convert('1')), cmap='gray')
	plt.axis('off')

	plt.subplot(2, 2, 2)
	plt.title('L')
	plt.imshow(np.array(Image.open(path).convert('L')), cmap='gray')
	plt.axis('off')

	plt.subplot(2, 2, 3)
	plt.title('RGB')
	plt.imshow(np.array(Image.open(path).convert('RGB')))
	plt.axis('off')

	img = np.array(Image.open(path).convert('L'))
	img = toZeroOne(img)
	plt.subplot(2, 2, 4)
	plt.title('ZeroOne')
	plt.imshow(img, cmap='gray')
	plt.axis('off')

	plt.show()

def show1(img):
	img.show()   # 先保存成临时图片文件, 然后使用操作系统默认图片浏览工具显示

def show2(imgData):
	plt.imshow(imgData)
	# plt.axis('off')
	plt.show()

def show3(imgData):
	from scipy.misc import toimage
	toimage(imgData).show()

def show4(imgData):
	from scipy.misc import imshow
	imshow(imgData)

def main():
	path = 'lena.jpg'
	showFlag = '2'
	if len(sys.argv) > 2:
		path = sys.argv[1]
		showFlag = sys.argv[2]

	img = Image.open(path)
	info(img)
	imgData = np.array(img)
	arrayInfo(imgData)

	if showFlag == '1':
		show1(img)
	elif showFlag == '2':
		show2(imgData)
	elif showFlag == '3':
		show3(imgData)
	elif showFlag == '4':
		show4(imgData)
	else:
		print 'Not found show function show%s' %(showFlag)

	showZeroOneImage(path)

	addSalt(path)

	showBlackWhiteImage(path)

if __name__ == '__main__':
	main()
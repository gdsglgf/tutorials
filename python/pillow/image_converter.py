#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image

def gray2rgb(data):
	return np.array(Image.fromarray(data, 'L').convert('RGB'))

# ITU-R 601-2 luma transform:
# 	L = R * 299/1000 + G * 587/1000 + B * 114/1000
def rgb2gray(data):
	return np.array(Image.fromarray(data, 'RGB').convert('L'))

def toGray(rgb):
	row, column, pipe = rgb.shape
	for i in range(row):
		for j in range(column):
			pix = rgb[i, j]
			r = pix[0]
			g = pix[1]
			b = pix[2]

			gray = (r * 299 + g * 587 + b * 114) / 1000

			print '%4d' %(gray),
		print

def main():
	rgb = np.array(np.arange(8 * 8 * 3).reshape((8, 8, 3)), dtype='uint8')
	print rgb
	print rgb2gray(rgb)
	toGray(rgb)

	Image.fromarray(rgb, 'RGB').save('rgb.jpg')
	img = np.array(Image.open('rgb.jpg'))
	print img    # 图片失真, 与rgb不同
	print rgb2gray(img)
	toGray(img)

if __name__ == '__main__':
	main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path = 'lena.jpg'

if len(sys.argv) >= 2:
	path = sys.argv[1]

print sys.argv

img = Image.open(path)  #打开图像
gray = img.convert('L')   #转换成灰度
r, g, b = img.split()   #分离三通道
pic = Image.merge('RGB', (r, g, b)) #合并三通道
plt.figure(path)
plt.subplot(2,3,1), plt.title('origin')
plt.imshow(np.array(img)), plt.axis('off')
plt.subplot(2,3,2), plt.title('gray')
plt.imshow(np.array(gray), cmap='gray'), plt.axis('off')
plt.subplot(2,3,3), plt.title('merge')
plt.imshow(np.array(pic)), plt.axis('off')
plt.subplot(2,3,4), plt.title('r')
plt.imshow(np.array(r), cmap='gray'), plt.axis('off')
plt.subplot(2,3,5), plt.title('g')
plt.imshow(np.array(g), cmap='gray'), plt.axis('off')
plt.subplot(2,3,6), plt.title('b')
plt.imshow(np.array(b), cmap='gray'), plt.axis('off')
plt.show()


print len(list(pic.getdata()))
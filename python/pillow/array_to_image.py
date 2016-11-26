from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def saveImage(data, mode, filename):
	img = Image.fromarray(data, mode)
	img.save(filename)

def createRGBImage():
	h, w = 128, 128
	data = np.zeros((h, w, 3), dtype=np.uint8)
	data[64, 64] = [255, 0, 0]

	return data

def createGreyscaleImage():
	h, w = 128, 128
	data = np.zeros((h, w), dtype=np.uint8)
	data[64, :] = 255
	data[:, 64] = 255
	return data

def createThumbnail():
	file = 'array_to_image_L.png'
	im = Image.open(file)
	im.thumbnail((32, 32))
	im.save("array_to_image_L.thumbnail.png")

if __name__ == '__main__':

	createThumbnail()

	# plt.figure('array to image')

	# # subplot 1
	# img1 = createRGBImage()
	# # saveImage(img1, 'RGB', 'array_to_image_RGB.png')
	# plt.subplot(1, 2, 1)
	# plt.title('RGB')
	# plt.imshow(img1)
	# # plt.axis('off')

	# # subplot 2
	# img2 = createGreyscaleImage()
	# # saveImage(img2, 'L', 'array_to_image_L.png')
	# plt.subplot(1, 2, 2)
	# plt.title('L')
	# plt.imshow(img2, interpolation='nearest')
	# plt.axis('off')

	# plt.show()
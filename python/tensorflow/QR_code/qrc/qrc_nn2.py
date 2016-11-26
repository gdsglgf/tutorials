# Quick Response Code Network

import os
from PIL import Image
import numpy as np
import tensorflow as tf

labels = ['0', '1']		# zero is have not 'LINE' sign, one is have 'LINE' sign
# data size
# 222 158
testRate = 0.2

length = 128 * 128

def filename(i):
	return 'image%s.jpg' %(i)

def readMappingData():
	imagesIds = []
	labels = []

	with open('dataset.txt') as f:
		for line in f:
			line = line.rstrip('\n')
			imageId, label = line.split(' ')
			imagesIds.append(imageId)
			labels.append(label)

	return imagesIds, labels

def oneHot(labelData):
	row = len(labelData)
	n = len(labels)

	data = np.zeros((row, n))
	for i in range(row):
		j = labels.index(labelData[i])
		data[i, j] = 1

	return data


def readDatasets(data_dir='data/'):
	imagesIds, labels = readMappingData()
	images = []
	row = len(labels)
	for i in imagesIds:
		fp = os.path.join(data_dir, filename(i))
		image = np.array(Image.open(fp))
		image = image.reshape(image.shape[0] * image.shape[1])

		# image = [1 if i >= 128 else 0 for i in image]

		images.extend(image)

	return np.array(images).reshape(row, length), oneHot(labels)

def buildDatasets():
	print 'start load data...'
	images, labels = readDatasets()
	print 'load data done...'

	print images.shape, labels.shape

	testSize = int(len(labels) * testRate)

	print testSize

	data = {'train': {
				'images': images[testSize : , :],
				'labels': labels[testSize : , :]
			},
		'test': {
				'images': images[0 : testSize, :],
				'labels': labels[0 : testSize, :]
			},
		'all': {
				'images': images,
				'labels': labels
			}
		}
	return data

def train():
	data = buildDatasets()

	sess = tf.InteractiveSession()

	# Create the model
	x = tf.placeholder(tf.float32, [None, length])
	W = tf.Variable(tf.zeros([length, 2]))
	b = tf.Variable(tf.zeros([2]))
	y = tf.nn.softmax(tf.matmul(x, W) + b)

	# Define loss and optimizer
	y_ = tf.placeholder(tf.float32, [None, 2])
	cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
	# train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
	train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
	correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

	# Train
	tf.initialize_all_variables().run()

	images, labels = data['train']['images'], data['train']['labels']
	print images.shape, labels.shape
	rows = images.shape[0]
	start = 0
	batch_size = 50
	for i in range(20000):
		if start >= rows:
			start = 0
		batch_xs, batch_ys = images[start : start + batch_size], labels[start : start + batch_size]
		start += batch_size
		if i%100 == 0:
			train_accuracy = accuracy.eval(feed_dict={x: batch_xs, y_: batch_ys})
			print("step %d, training accuracy %g" %(i, train_accuracy))
		train_step.run({x: batch_xs, y_: batch_ys})

	# Test trained model
	print("test accuracy %g" %accuracy.eval({x: data['test']['images'], y_: data['test']['labels']}))
	print("train accuracy %g" %accuracy.eval({x: data['train']['images'], y_: data['train']['labels']}))
	print("all accuracy %g" %accuracy.eval({x: data['all']['images'], y_: data['all']['labels']}))

	sess.close()

def main():
	train()

def peekImage():
	image = Image.open('data/image0.jpg')
	data = np.array(image)
	row, column = data.shape
	print row, column
	for i in range(row):
		for j in range(column):
			print data[i, j],
		print

if __name__ == '__main__':
	main()
	# buildDatasets()

	

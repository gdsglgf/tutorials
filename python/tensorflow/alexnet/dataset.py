import collections
from datetime import datetime
import os
import sys

# third party lib
import numpy
from PIL import Image

from image_reader import ImageReader
from label_util import listdir, filename_to_label, dense_to_one_hot

Datasets = collections.namedtuple('Datasets', ['train', 'validation', 'test'])

class DataSet(object):
	def __init__(self, images, labels):
		assert images.shape[0] == labels.shape[0], (
			'images.shape: %s labels.shape: %s' % (images.shape, labels.shape))

		self._num_examples = images.shape[0]

		# Convert from [0, 255] -> [0.0, 1.0].
		images = images.astype(numpy.float32)
		images = numpy.multiply(images, 1.0 / 255.0)

		self._images = images
		self._labels = labels
		self._epochs_completed = 0
		self._index_in_epoch = 0

	@property
	def images(self):
		return self._images

	@property
	def labels(self):
		return self._labels

	@property
	def num_examples(self):
		return self._num_examples

	@property
	def epochs_completed(self):
		return self._epochs_completed

	def next_batch(self, batch_size):
		"""Return the next `batch_size` examples from this data set."""
		start = self._index_in_epoch
		self._index_in_epoch += batch_size
		if self._index_in_epoch > self._num_examples:
			# Finished epoch
			self._epochs_completed += 1
			# Shuffle the data
			perm = numpy.arange(self._num_examples)
			numpy.random.shuffle(perm)
			self._images = self._images[perm]
			self._labels = self._labels[perm]
			# Start next epoch
			start = 0
			self._index_in_epoch = batch_size
			assert batch_size <= self._num_examples
		end = self._index_in_epoch
		return self._images[start:end], self._labels[start:end]

def read_data(data_dir):
	filenames = listdir(data_dir)
	num_file = len(filenames)
	print '%s: read data from %s: total %d files.' %(datetime.now(), data_dir, num_file)
	images = numpy.array([])
	size = (227, 227)

	for i, f in enumerate(filenames, start=1):
		image = numpy.array(Image.open(f).convert('RGB').resize(size))
		images = numpy.append(images, image)
		os.write(1, "\rreading %d/%d, %s" %(i, num_file, f))
		sys.stdout.flush()
	print

	labels = filename_to_label(filenames)
	labels = numpy.array(labels)
	return images.reshape(-1, 227, 227, 3), dense_to_one_hot(labels)

def read_data_sets(train_dir='train', validation_dir='validation', test_dir='test'):
	train_images, train_labels = read_data(train_dir)
	train = DataSet(train_images, train_labels)

	validation_images, validation_labels = read_data(validation_dir)
	validation = DataSet(validation_images, validation_labels)

	test_images, test_labels = read_data(test_dir)
	test = DataSet(test_images, test_labels)

	return Datasets(train=train, validation=validation, test=test)

def map_reduce_read_data(data_dir):
	filenames = listdir(data_dir)
	print '%s: read data from %s: total %d files.' %(datetime.now(), data_dir, len(filenames))
	filenames = numpy.array(filenames)
	# Shuffle the data
	perm = numpy.arange(filenames.shape[0])
	numpy.random.shuffle(perm)
	filenames = filenames[perm]
	
	ir = ImageReader()
	images, labels = ir.read_data(filenames, one_hot=True)

	print images.shape, labels.shape
	return images, labels 

def map_reduce_load_datasets(train_dir='train', validation_dir='validation', test_dir='test'):
	train_images, train_labels = map_reduce_read_data(train_dir)
	train = DataSet(train_images, train_labels)

	validation_images, validation_labels = map_reduce_read_data(validation_dir)
	validation = DataSet(validation_images, validation_labels)

	test_images, test_labels = map_reduce_read_data(test_dir)
	test = DataSet(test_images, test_labels)

	return Datasets(train=train, validation=validation, test=test)

def load_datasets(train_dir='train', validation_dir='validation', test_dir='test'):
	return map_reduce_load_datasets(train_dir, validation_dir, test_dir)

def test_read_data():
	images, labels = read_data('temp')
	print images.shape, labels.shape
	print labels

def test_map_reduce_read_data():
	test_images, test_labels = map_reduce_read_data('temp')
	print test_images.shape, test_labels.shape

if __name__ == '__main__':
	# load_datasets()

	test_read_data()
	test_map_reduce_read_data()


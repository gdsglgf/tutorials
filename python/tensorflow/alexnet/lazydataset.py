import os

# third party lib
import numpy

from image_reader import ImageReader

class LazyDataSet(object):
	def __init__(self, data_dir, label=None, batch_size=128):
		filenames = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]
		if label:
			filenames = [f for f in filenames if f.startswith(label)]
			print('label: %s' %(label))
		filenames = [os.path.join(data_dir, f) for f in filenames]
		self._filenames = numpy.array(filenames)
		self._num_examples = self._filenames.shape[0]

		assert batch_size <= self._num_examples, ('batch_size: %d, num_examples: %d' %(batch_size, self._num_examples))
		self._batch_size = batch_size

		self._epochs_completed = 0
		self._index_in_epoch = 0
		self._reader = ImageReader(info_on=False)

		self.shuffle_data()

	@property
	def num_examples(self):
		return self._num_examples

	@property
	def epochs_completed(self):
		return self._epochs_completed

	@property
	def num_epochs(self):
		return self._num_examples // self._batch_size

	@property
	def batch_size(self):
		return self._batch_size

	def shuffle_data(self):
		perm = numpy.arange(self._num_examples)
		numpy.random.shuffle(perm)
		self._filenames = self._filenames[perm]

	def next_batch(self, one_hot=False):
		start = self._index_in_epoch
		self._index_in_epoch += self._batch_size
		if self._index_in_epoch > self._num_examples:
			# Finished epoch
			self._epochs_completed += 1
			# Shuffle the data
			self.shuffle_data()
			# Start next epoch
			start = 0
			self._index_in_epoch = self._batch_size
		end = self._index_in_epoch
		return self._reader.read_data(self._filenames[start:end], one_hot=one_hot)
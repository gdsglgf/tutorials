import os

import numpy

class_names = ['label01', 'label02', 'label03', 'label04', 'label05']
num_classes = len(class_names)image

def listdir(data_dir, suffix='.jpg'):
	filenames = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(suffix)]
	return filenames

def dense_to_one_hot(labels_dense, num_classes=num_classes):
	"""Convert class labels from scalars to one-hot vectors."""
	num_labels = labels_dense.shape[0]
	index_offset = numpy.arange(num_labels) * num_classes
	labels_one_hot = numpy.zeros((num_labels, num_classes))
	labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
	return labels_one_hot

def extract_label(filename):
	class_name = filename.split('/')[-1].split('_')[0]
	return class_names.index(class_name)

def filename_to_label(filename_list):
	labels = [extract_label(f) for f in filename_list]
	return labels

def test_labels_one_hot():
	labels_dense = numpy.array([0, 1, 2, 0, 1])
	labels_one_hot = dense_to_one_hot(labels_dense, 3)
	print labels_one_hot

def test_extract_label():
	fname = 'PP01_123.jpg'
	print fname, extract_label(fname)

	fname = 'test_123.jpg'
	print fname, extract_label(fname)

if __name__ == '__main__':
	test_labels_one_hot()
	test_extract_label()
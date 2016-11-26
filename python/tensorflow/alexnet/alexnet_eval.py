import os

import numpy as np
from PIL import Image
import tensorflow as tf

from label_util import class_names, num_classes, listdir, filename_to_label
from alexnet import inference
from lazydataset import LazyDataSet

def weight_variable():
	weights = {
		'wc1': tf.Variable(tf.zeros([11, 11, 3, 64]), name='wc1'),
		'wc2': tf.Variable(tf.zeros([5, 5, 64, 192]), name='wc2'),
		'wc3': tf.Variable(tf.zeros([3, 3, 192, 384]), name='wc3'),
		'wc4': tf.Variable(tf.zeros([3, 3, 384, 256]), name='wc4'),
		'wc5': tf.Variable(tf.zeros([3, 3, 256, 256]), name='wc15'),
		'wfc6': tf.Variable(tf.zeros([6*6*256, 4096]), name='wfc6'),
		'wfc7': tf.Variable(tf.zeros([4096, 4096]), name='wfc7'),
		'wfc8': tf.Variable(tf.zeros([4096, 4]), name='wfc8')
	}
	return weights

def bias_variable():
	biases = {
		'bc1': tf.Variable(tf.zeros([64]), name='bc1'),
		'bc2': tf.Variable(tf.zeros([192]), name='bc2'),
		'bc3': tf.Variable(tf.zeros([384]), name='bc3'),
		'bc4': tf.Variable(tf.zeros([256]), name='bc4'),
		'bc5': tf.Variable(tf.zeros([256]), name='bc5'),
		'bfc6': tf.Variable(tf.zeros([4096]), name='bfc6'),
		'bfc7': tf.Variable(tf.zeros([4096]), name='bfc7'),
		'bfc8': tf.Variable(tf.zeros([4]), name='bfcb')
	}
	return biases

def eval_once(output, labels):
	rank = np.argsort(output)
	true_count = 0
	for i in range(output.shape[0]):
		inds = rank[i, :]
		if labels[i] == inds[-1]:
			true_count += 1
	return true_count

def evaluate(images, checkpoint_dir):
	weights = weight_variable()
	biases = bias_variable()
	x = tf.placeholder(tf.float32, [None, 227, 227, 3])
	y = tf.placeholder(tf.float32, [None, num_classes])
	keep_prob = tf.placeholder(tf.float32)

	pred = inference(x, weights, biases, keep_prob)

	saver = tf.train.Saver()
	with tf.Session() as sess:
		ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
		if ckpt and ckpt.model_checkpoint_path:
			print 'load model %s' %(ckpt.model_checkpoint_path)
			saver.restore(sess, ckpt.model_checkpoint_path)
		else:
			print('No checkpoint file found at %s' % checkpoint_dir)
		output = sess.run(pred, feed_dict={x: images, keep_prob: 1.})
	return output

def evaluate_all(data_dir, checkpoint_dir=None, model_checkpoint_path=None):
	weights = weight_variable()
	biases = bias_variable()
	x = tf.placeholder(tf.float32, [None, 227, 227, 3])
	y = tf.placeholder(tf.float32, [None, num_classes])
	keep_prob = tf.placeholder(tf.float32)

	pred = inference(x, weights, biases, keep_prob)

	saver = tf.train.Saver()
	with tf.Session() as sess:
		if checkpoint_dir:
			ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
			if ckpt and ckpt.model_checkpoint_path:
				print 'load latest model %s' %(ckpt.model_checkpoint_path)
				saver.restore(sess, ckpt.model_checkpoint_path)
			else:
				print('No checkpoint file found at %s' % checkpoint_dir)
				return
		elif model_checkpoint_path:
			print 'load model %s' %(model_checkpoint_path)
			saver.restore(sess, model_checkpoint_path)
		else:
			return

		dataset = LazyDataSet(data_dir=data_dir, batch_size=50)
		true_count = 0
		for i in range(dataset.num_epochs):
			images, labels = dataset.next_batch()
			output = sess.run(pred, feed_dict={x: images, keep_prob: 1.})

			batch_true_count = eval_once(output, labels)
			true_count += batch_true_count
			print('step:%d, %d/%d, accuracy: %g' %(i, batch_true_count, dataset.batch_size, batch_true_count * 1.0 / dataset.batch_size))

		num_examples = dataset.num_epochs * dataset.batch_size
		print('%d/%d, accuracy: %g' %(true_count, num_examples, true_count * 1.0 / num_examples))

def evalate_by_class(data_dir, checkpoint_dir=None, model_checkpoint_path=None):
	weights = weight_variable()
	biases = bias_variable()
	x = tf.placeholder(tf.float32, [None, 227, 227, 3])
	y = tf.placeholder(tf.float32, [None, num_classes])
	keep_prob = tf.placeholder(tf.float32)

	pred = inference(x, weights, biases, keep_prob)

	saver = tf.train.Saver()
	with tf.Session() as sess:
		if checkpoint_dir:
			ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
			if ckpt and ckpt.model_checkpoint_path:
				print 'load latest model %s' %(ckpt.model_checkpoint_path)
				saver.restore(sess, ckpt.model_checkpoint_path)
			else:
				print('No checkpoint file found at %s' % checkpoint_dir)
				return
		elif model_checkpoint_path:
			print 'load model %s' %(model_checkpoint_path)
			saver.restore(sess, model_checkpoint_path)
		else:
			return

		total_true = 0
		total_examples = 0
		for name in class_names:
			dataset = LazyDataSet(data_dir=data_dir, label=name, batch_size=50)
			true_count = 0
			for i in range(dataset.num_epochs):
				images, labels = dataset.next_batch()
				output = sess.run(pred, feed_dict={x: images, keep_prob: 1.})

				batch_true_count = eval_once(output, labels)
				true_count += batch_true_count
				print('step:%d, %d/%d, accuracy: %g' %(i, batch_true_count, dataset.batch_size, batch_true_count * 1.0 / dataset.batch_size))
			num_examples = dataset.num_epochs * dataset.batch_size
			print('class:%s, %d/%d, accuracy: %g' %(name, true_count, num_examples, true_count * 1.0 / num_examples))
			total_true += true_count
			total_examples += num_examples
		print('%d/%d, total accuracy: %g' %(total_true, total_examples, total_true * 1.0 / total_examples))

def evaluate_all_checkpoint(data_dir, checkpoint_dir):
	ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
	if ckpt and ckpt.model_checkpoint_path:
		print ckpt.model_checkpoint_path
		print ckpt.all_model_checkpoint_paths
		for checkpoint in ckpt.all_model_checkpoint_paths:
			# evaluate_all(data_dir, model_checkpoint_path=checkpoint)
			evalate_by_class(data_dir, model_checkpoint_path=checkpoint)
	else:
		print('No checkpoint file found at %s' % checkpoint_dir)
		return

def read_image(data_dir='temp/'):
	filenames = listdir(data_dir)
	labels = filename_to_label(filenames)
	images = []
	for f in filenames:
		img = Image.open(f).convert('RGB').resize((227, 227))
		images.append(np.array(img))

	images = np.array(images)
	print(images.shape)

	return filenames, images, labels

def test_model():
	filenames, images, labels = read_image()
	output = evaluate(images)

	rank = np.argsort(output)
	true_classify = []
	false_classify = []
	for i in range(output.shape[0]):
		inds = rank[i, :]
		print "Image", i, filenames[i]
		for j in range(num_classes):
			print inds[-1-j], output[i, inds[-1-j]]
		
		matched = labels[i] == inds[-1]
		if matched:
			true_classify.append(filenames[i])
		else:
			false_classify.append(filenames[i])
		print('class: %s, label: %d, predicted: %d, matching: %s' %(class_names[labels[i]], labels[i], inds[-1], matched))

	print('true classify: %d %s' %(len(true_classify), true_classify))
	print('false classify: %d %s' %(len(false_classify), false_classify))
	print('accuracy(%d/%d): %g' %(len(true_classify), len(filenames), len(true_classify) * 1.0 / len(filenames)))

def test_checkpoint():
	checkpoint_dir = 'model_20161026141622/'
	ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
	if ckpt and ckpt.model_checkpoint_path:
		print ckpt.model_checkpoint_path
		print ckpt.all_model_checkpoint_paths

		path1 = 'model_20161026141622/model.ckpt-160'
		print(path1 in ckpt.all_model_checkpoint_paths)

		path2 = 'tttmodel_20161026141622/model.ckpt-160'
		print(path2 in ckpt.all_model_checkpoint_paths)
	else:
		print('No checkpoint file found at %s' % checkpoint_dir)
		return

		



if __name__ == '__main__':
	# test_model()
	# test_checkpoint()

	checkpoint_dir = 'model_20161026141622/'
	model_checkpoint_path = 'model_20161026141622/model.ckpt-160'

	# evaluate_all('test/', model_checkpoint_path=model_checkpoint_path)
	# evalate_by_class('test/', checkpoint_dir)
	# evalate_by_class('validation/', checkpoint_dir)
	# evalate_by_class('train/', checkpoint_dir)
	# evalate_by_class('data/', checkpoint_dir)
	
	evaluate_all_checkpoint('test', 'model_20161028162548')
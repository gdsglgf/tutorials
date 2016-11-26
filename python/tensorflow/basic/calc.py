from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

def run(a, b):
	with tf.Session() as sess:
		correct_prediction = tf.equal(a, b)
		result = sess.run(correct_prediction)
		print(result)
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		print(accuracy.eval())
		print(sess.run(accuracy))

if __name__ == '__main__':
	a = tf.constant([0, 1])
	b = tf.constant([1, 1])
	run(a, b)
	
	c = tf.constant([[0, 0], [1, 1]])
	d = tf.constant([[1, 0], [3, 4]])
	run(c, d)
	
	i = tf.constant([0, 0, 1, 1])
	j = tf.constant(['0', '0', '1', '1'])
	run(i, j)

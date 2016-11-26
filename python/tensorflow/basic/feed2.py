import tensorflow as tf

v1 = tf.placeholder(tf.float32, name='x')
v2 = tf.placeholder(tf.float32, name='y')

sums = tf.add(v1, v2)
mul = tf.mul(v1, v2)

with tf.Session() as sess:
	print sess.run([sums, mul], feed_dict={v1: 2, v2: 3})
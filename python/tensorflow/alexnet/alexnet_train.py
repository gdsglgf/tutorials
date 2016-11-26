from datetime import datetime
import os
import time

import tensorflow as tf

from dataset import load_datasets
from label_util import num_classes
from alexnet import parameters, inference

now = datetime.now().strftime("%Y%m%d%H%M%S")
model_dir = 'model_%s' %(now)
os.mkdir(model_dir)
checkpoint_path = os.path.join(model_dir, 'model.ckpt')
print('checkpoint path: %s' %(checkpoint_path))

data = load_datasets()

learning_rate = 0.05
dropout = 0.8
training_iters = 20000
batch_size = 64
display_step = 10


x = tf.placeholder(tf.float32, [None, 227, 227, 3])
y = tf.placeholder(tf.float32, [None, num_classes])
keep_prob = tf.placeholder(tf.float32)

weights, biases = parameters()

pred = inference(x, weights, biases, keep_prob)

# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
# optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

softmax_linear = tf.nn.softmax(pred)
cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(softmax_linear + 1e-10), reduction_indices=[1]))

# softmax_linear =  = tf.nn.log_softmax(pred)
# cost = -tf.reduce_sum(y * softmax_linear)

optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.initialize_all_variables()
saver = tf.train.Saver()
max_acc = 0
max_step = 0
with tf.Session() as sess:
	checkpoint_dir = 'model_20161026141622/'
	ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
	if ckpt and ckpt.model_checkpoint_path:
		print('load model %s' %(ckpt.model_checkpoint_path))
		saver.restore(sess, ckpt.model_checkpoint_path)
		global_step = int(ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1])
	else:
		print('No checkpoint file found at %s' % checkpoint_dir)
		print('start new training...')
		global_step = 0
		sess.run(init)

	step = 1
	while step <= training_iters:
		batch_xs, batch_ys = data.train.next_batch(batch_size)
		start_time = time.time()
		sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys, keep_prob: dropout})
		duration = time.time() - start_time

		if step % display_step == 0:
			acc = sess.run(accuracy, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.})
			loss = sess.run(cost, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.})

			examples_per_sec = batch_size / duration
			sec_per_batch = float(duration)
			print ('%s: step %d , loss = %.5f, training accuracy = %.5f (%.1f examples/sec; %.3f sec/batch)' 
				%(datetime.now(), step, loss, acc, examples_per_sec, sec_per_batch))
			
			if acc > max_acc:
				max_acc = acc
				max_step = step
				saver.save(sess, checkpoint_path, global_step=global_step + step)
				print('%s: step %d : save model done.' %(datetime.now(), step))
				print(sess.run(biases['bfc8']))


		if step % 100 == 0:
			validation_acc, validation_loss = sess.run([accuracy, cost], feed_dict={x: data.validation.images, y: data.validation.labels, keep_prob: 1.})
			print('%s: step %d : loss = %.5f , validation accuracy = %.5f' % (datetime.now(), step, validation_loss, validation_acc))
			if max_step != step:
				saver.save(sess, checkpoint_path, global_step=global_step + step)

		step += 1
	print "Optimization Finished!"
	print step, sess.run(biases['fc8'])
	print "Testing Accuracy:", sess.run(accuracy, feed_dict={x: data.test.images, y: data.test.labels, keep_prob: 1.})
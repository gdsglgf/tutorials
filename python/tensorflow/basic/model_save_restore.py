import sys
import tensorflow as tf

def save_model():
	v1 = tf.Variable(1.1, name="v1")
	v2 = tf.Variable(1.2, name="v2")
	v3 = tf.Variable('hello world', name='hello')

	init = tf.initialize_all_variables()
	saver = tf.train.Saver()
	# saver = tf.train.Saver({"v1": v1, "v2": v2, "hello": v3})
	with tf.Session() as sess:
		sess.run(init)
		print v2.eval(sess)
		save_path = "model.ckpt"
		saver.save(sess,save_path)
		print "Model stored...."

def restore():
	v3 = tf.Variable(0.0, name="v1")
	v4 = tf.Variable(0.0, name="v2")
	hello = tf.Variable('', name='hello')
	saver = tf.train.Saver()

	with tf.Session() as sess:
		save_path = "model.ckpt"
		saver.restore(sess, save_path)
		print("Model restored.")
		print sess.run(v3)

		# hello1 = tf.get_collection('hello')
		# print hello1
		
		print hello
		print sess.run(hello)

def export_meta_graph():
	hello = tf.constant('Hello, TensorFlow!', name='hello')
	init = tf.initialize_all_variables()
	saver = tf.train.Saver()
	tf.add_to_collection('train_op', hello)
	with tf.Session() as sess:
		sess.run(init)
		meta_graph_def = tf.train.export_meta_graph(
			filename='my-model-10000.meta',
			collection_list=["hello"])
		saver.save(sess, 'my-model', global_step=10000)

def import_meta_graph():
	with tf.Session() as sess:
		new_saver = tf.train.import_meta_graph('my-model-10000.meta')
		new_saver.restore(sess, 'my-model-10000')
		# tf.get_collection() returns a list. In this example we only want the
		# first one.
		hello = tf.get_collection('train_op')[0]
		print len(tf.get_collection('train_op'))
		print sess.run(hello)

if __name__ == '__main__':
	command = ''
	if len(sys.argv) >= 2:
		command = sys.argv[1]
	if command == '1':
		restore()
		import_meta_graph()
	else:
		save_model()
		export_meta_graph()
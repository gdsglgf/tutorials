import os
from Queue import Queue
import sys
from threading import Thread
import time

# third party lib
import numpy
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from label_util import listdir, filename_to_label, dense_to_one_hot

class ImageReader(object):
	"""ImageReader - read image data"""
	def __init__(self, num_worker_threads=5, info_on=True):
		super(ImageReader, self).__init__()
		self.num_worker_threads = num_worker_threads
		self.size = (227, 227)
		self.info_on = info_on

	def create_queue(self, input_list):
		output_queue = Queue()
		for item in input_list:
			output_queue.put(item)
		return output_queue

	def read_data(self, filenames, one_hot=False):
		input_queue = self.create_queue(filenames)
		output_queue = self.process_queue(input_queue)

		filenames = []
		images = []
		while not output_queue.empty():
			fname, img = output_queue.get()
			filenames.append(fname)
			images.append(img)

		labels = filename_to_label(filenames)

		images = numpy.array(images)
		labels = numpy.array(labels)

		if one_hot:
			labels = dense_to_one_hot(labels)

		images = images.astype(numpy.float32)
		images = numpy.multiply(images, 1.0 / 255.0)
		return images, labels

	def process_queue(self, input_queue):
		output_queue = Queue()
		total = input_queue.qsize()
		def worker():
			while not input_queue.empty():
				fname = input_queue.get()
				current = input_queue.qsize()
				if self.info_on:
					os.write(1, '\rprocess(%d/%d): %s...' %(total - current, total, fname))
					sys.stdout.flush()
				image = numpy.array(Image.open(fname).convert('RGB').resize(self.size))
				output_queue.put((fname, image))	# add a tuple(filename, image) to output queue
				input_queue.task_done()
		for i in range(self.num_worker_threads): # start threads
			worker_thread = Thread(target=worker)
			worker_thread.daemon = True
			worker_thread.start()
		input_queue.join() # block until all tasks are done
		if self.info_on:
			print	# end of the flush

		return output_queue

def main():
	data_dir = 'train/'
	filenames = listdir(data_dir)

	ir = ImageReader()
	images, labels = ir.read_data(filenames[:200])
	print images.shape, labels.shape

if __name__ == '__main__':
	main()
import os
import sys
from urllib import urlretrieve
import csv
from Queue import Queue
from threading import Thread
import time

# third party lib
from PIL import Image

# variable shared by both producer and consumer
# producer put item
# consumer get item
message_queue = Queue()		# item in the queue is a tuple(file_path, image_url)

class ProducerThread(Thread):
	def __init__(self, csv, work_directory):
		Thread.__init__(self)
		self.csv = csv
		self.work_directory = work_directory
		self.counter = {}

		self.maybe_mkdir()

	def maybe_mkdir(self):
		if not self.work_directory:
			self.work_directory = 'data/'	# set default
		if not os.path.exists(self.work_directory):
			os.mkdir(self.work_directory)

	def filename(self, label, count):
		return os.path.join(self.work_directory, '%s_%d.jpg' %(label, count))

	def run(self):
		global message_queue
		with open(self.csv) as csvfile:
			reader = csv.DictReader(csvfile)
			# seq,image_url,label
			step = 0
			for row in reader:
				image_url = row['image_url']
				label = row['label']

				count = self.counter.get(label, 0)
				self.counter[label] = count + 1
				path = os.path.join(self.work_directory, '%s_%d.jpg' %(label, count))

				message_queue.put((path, image_url))
				step += 1
				os.write(1, '\rProducer - step: %d, put: %s, size: %d' %(step, path, message_queue.qsize()))
				sys.stdout.flush()
			print('\nProducer done...')

	def show_counter(self):
		for key, value in self.counter.items():
			print key, value

class ConsumerThread(Thread):
	def __init__(self, name):
		Thread.__init__(self)
		self.name = name

	def is_valid(self, path):
		status = True
		try:
			img = Image.open(path)
		except:
			status = False
		return status

	def maybe_download(self, url, path):
		if not os.path.exists(path):
			urlretrieve(url, path)
		elif not self.is_valid(path):
			if os.path.exists(path):
				os.remove(path)
				os.write(1, '\rremove file %s' %(path))
				sys.stdout.flush()
			urlretrieve(url, path)

	def run(self):
		global message_queue
		while not message_queue.empty():
			path, image_url = message_queue.get()
			remain_size = message_queue.qsize()
			message_queue.task_done()
			self.maybe_download(image_url, path)
			os.write(1, '\r%s Consumer : %s, size: %d' %(self.name, path, remain_size))
			sys.stdout.flush()
		print('\nConsumer %s done...' %(self.name))

def download(csv, work_directory):
	producer = ProducerThread(csv, work_directory)
	producer.start()

	time.sleep(1)
	num_worker_threads = 5
	workers = []
	for i in range(num_worker_threads):
		worker_thread = ConsumerThread('Thread-%d' %(i))
		worker_thread.daemon = True
		worker_thread.start()
		workers.append(worker_thread)

	message_queue.join() # block until all tasks are done
	for worker in workers:
		worker.join()

	producer.show_counter()

if __name__ == '__main__':
	csv = 'image_dataset.csv'
	work_directory = 'data/'
	download(csv, work_directory)

import os
from Queue import Queue
import sys
from threading import Thread
import time

class DataReader(object):
	"""DataReader - simple data reader"""
	def __init__(self, num_worker_threads=5):
		super(DataReader, self).__init__()
		self.num_worker_threads = num_worker_threads

	def read_data(self, filenames):
		input_queue = Queue()
		for item in filenames:
			input_queue.put(item)

		output_queue = self.process_queue(input_queue)
		output = []
		while not output_queue.empty():
			output.append(output_queue.get())
		print(output)

	def process_queue(self, input_queue):
		output_queue = Queue()
		total = input_queue.qsize()
		def worker():
			while not input_queue.empty():
				item = input_queue.get()
				current = input_queue.qsize()
				os.write(1, '\rprocess(%d/%d): %s...' %(total - current, total, item))
				sys.stdout.flush()
				with open(item) as f:
					data = f.readlines()
				output_queue.put((item, data))
				input_queue.task_done()
				time.sleep(1)	# sleep 1 second to see flush demo
		for i in range(self.num_worker_threads): # start threads
			worker_thread = Thread(target=worker)
			worker_thread.daemon = True
			worker_thread.start()
		input_queue.join() # block until all tasks are done
		print

		return output_queue

def main():
	data_dir = 'tmp/'
	filenames = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.txt')]
	print(filenames)

	dr = DataReader()

	dr.read_data(filenames)

if __name__ == '__main__':
	main()
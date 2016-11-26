import threading
import Queue
import operator
import os
import sys

class MapReduce:
    ''' MapReduce - to use, subclass by defining these functions,
                    then call self.map_reduce():
        parse_fn(self, k, v) => [(k, v), ...]
        map_fn(self, k, v) => [(k, v1), (k, v2), ...]
        reduce_fn(self, k, [v1, v2, ...]) => [(k, v)]
        output_fn(self, [(k, v), ...])
    '''
    def __init__(self):
        self.data = None
        self.num_worker_threads = 5
    
    class SynchronizedDict(): # we need this for merging
        def __init__(self):
            self.lock = threading.Lock()
            self.d = {}
        def isin(self, k):
            with self.lock:
                if k in self.d:
                    return True
                else:
                    return False
        def get(self, k):
            with self.lock:
                return self.d[k]
        def set(self, k, v): # we don't need del
            with self.lock:
                self.d[k] = v
        def set_append(self, k, v): # for thread-safe list append
            with self.lock:
                self.d[k].append(v)
        def items(self):
            with self.lock:
                return self.d.items()

    def create_queue(self, input_list): # helper fn for queues
        output_queue = Queue.Queue()
        for value in input_list:
            output_queue.put(value)
        return output_queue

    def create_list(self, input_queue): # helper fn for queues
        output_list = []
        while not input_queue.empty():
            item = input_queue.get()
            output_list.append(item)
            input_queue.task_done()
        return output_list

    def merge_fn(self, k, v, merge_dict): # helper fn for merge
        if merge_dict.isin(k):
            merge_dict.set_append(k, v)
        else:
            merge_dict.set(k, [v])

    def process_queue(self, input_queue, fn_selector): # helper fn
        output_queue = Queue.Queue()
        if fn_selector == 'merge':
            merge_dict = self.SynchronizedDict()
        def worker():
            while not input_queue.empty():
                (k, v) = input_queue.get()
                if fn_selector in ['map', 'reduce']:
                    if fn_selector == 'map':
                        result_list = self.map_fn(k, v)
                    elif fn_selector == 'reduce':
                        result_list = self.reduce_fn(k, v)
                    for result_tuple in result_list: # flatten
                        output_queue.put(result_tuple)
                elif fn_selector == 'merge': # merge v to same k
                    self.merge_fn(k, v, merge_dict)
                else:
                    raise Exception, "Bad fn_selector="+fn_selector
                input_queue.task_done()
        for i in range(self.num_worker_threads): # start threads
            worker_thread = threading.Thread(target=worker)
            worker_thread.daemon = True
            worker_thread.start()
        input_queue.join() # wait for worker threads to finish
        if fn_selector == 'merge':
            output_list = sorted(merge_dict.items(), key=operator.itemgetter(0))
            output_queue = self.create_queue(output_list)
        return output_queue

    def map_reduce(self): # the actual map-reduce algoritm
        data_list = self.parse_fn(self.data)
        data_queue = self.create_queue(data_list) # enqueue the data so we can multi-process
        map_queue = self.process_queue(data_queue, 'map') # [(k,v),...] => [(k,v1),(k,v2),...]

        # do not need merge and reduce
        # merge_queue = self.process_queue(map_queue, 'merge') # [(k,v1),(k,v2),...] => [(k,[v1,v2,...]),...]
        # reduce_queue = self.process_queue(merge_queue, 'reduce') # [(k,[v1,v2,...]),...] => [(k,v),...]

        output_list = self.create_list(map_queue) # deque into list for output handling
        return self.output_fn(output_list)

class DataReader(MapReduce):
    """DataReader - simple read data content"""
    def __init__(self, filenames):
        MapReduce.__init__(self)
        self.data = filenames

    def parse_fn(self, data): # break string into [(k, v), ...] tuples for each line
        data_list = map(lambda filename: (None, filename), data)
        return data_list

    def map_fn(self, key, filename): # return (filename, content) tuples for each file, ignore key
        os.write(1, '\rmap file: %s' %(filename))
        sys.stdout.flush()
        with open(filename) as f:
            data = f.readlines()
        return [(filename, data)]

    def reduce_fn(self, filename, data): # just return data
        return [(filename, data)]

    def output_fn(self, output_list): # just return
        return output_list

def create_test_file(data_dir):
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        for i in range(0, 20):
            filename = 'file%d.txt' %(i)
            fp = os.path.join(data_dir, filename)
            with open(fp, 'w') as f:
                f.write('file %d' %(i))

def main():
    data_dir = 'tmp/'
    create_test_file(data_dir)
    filenames = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.txt')]
    print(filenames)

    dr = DataReader(filenames)

    content = dr.map_reduce()
    print
    print(content)
    print(len(content))

if __name__ == '__main__':
    main()
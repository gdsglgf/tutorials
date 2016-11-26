from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

filename = '/tmp/cifar10_data/cifar-10-batches-bin/data_batch_1.bin'
h, w = 32, 32

LABELS = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

counter = 0
with open(filename, "r") as f:
	while True:
		label = f.read(1)
		if label == "":
			break # end of file
		r = [int(i.encode("hex"), 16) for i in f.read(1024)]
		g = [int(i.encode("hex"), 16) for i in f.read(1024)]
		b = [int(i.encode("hex"), 16) for i in f.read(1024)]

		data = np.zeros((h, w, 3), dtype=np.uint8)
		for i in range(h):
			for j in range(w):
				index = i * w + j
				data[i, j] = [np.uint8(r[index]), np.uint8(g[index]), np.uint8(b[index])]

		# plt.imshow(data, interpolation='nearest')
		# plt.show()

		img = Image.fromarray(data, 'RGB')
		path = '%d_%d.png' %(counter, int(label.encode("hex"),16))
		img.save('cifar10_data/data_batch_1/' + path)

		print 'save Image', path
		counter += 1
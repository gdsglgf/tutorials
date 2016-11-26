from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print type(mnist.train.images)
print mnist.train.images.shape
print mnist.train.labels.shape
print mnist.validation.images.shape
print mnist.validation.labels.shape
print mnist.test.images.shape
print mnist.test.labels.shape

# <type 'numpy.ndarray'>
# (55000, 784)
# (55000, 10)
# (5000, 784)
# (5000, 10)
# (10000, 784)
# (10000, 10)

img = mnist.train.images[0].reshape((28, 28))
print img
print mnist.train.labels[0]

plt.imshow(img, cmap='gray')
plt.show()
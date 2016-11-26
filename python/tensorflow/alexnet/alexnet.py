
import tensorflow as tf

def weight_variable(shape, name):
  # initial = tf.truncated_normal(shape, stddev=0.1)
  initial = tf.random_normal(shape)
  return tf.Variable(initial, name=name)

def bias_variable(shape, name):
  # initial = tf.constant(0.1, shape=shape)
  initial = tf.random_normal(shape)
  return tf.Variable(initial, name=name)

def conv2d(x, kernel, strides, biases, name):
  return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(x, kernel, strides=strides, padding='SAME'), biases), name=name)

def max_pool(x, name):
  return tf.nn.max_pool(x, 
                        ksize=[1, 3, 3, 1], 
                        strides=[1, 2, 2, 1], 
                        padding='VALID', 
                        name=name)

def print_activations(t):
  print(t.op.name, ' ', t.get_shape().as_list())

def parameters():
  weights = {
    'wc1': weight_variable([11, 11, 3, 64], 'wc1'),
    'wc2': weight_variable([5, 5, 64, 192], 'wc2'),
    'wc3': weight_variable([3, 3, 192, 384], 'wc3'),
    'wc4': weight_variable([3, 3, 384, 256], 'wc4'),
    'wc5': weight_variable([3, 3, 256, 256], 'wc5'),
    'wfc6': weight_variable([6*6*256, 4096], 'wfc6'),
    'wfc7': weight_variable([4096, 4096], 'wfc7'),
    'wfc8': weight_variable([4096, 4], 'wfc8')
  }
  biases = {
    'bc1': bias_variable([64], 'bc1'),
    'bc2': bias_variable([192], 'bc2'),
    'bc3': bias_variable([384], 'bc3'),
    'bc4': bias_variable([256], 'bc4'),
    'bc5': bias_variable([256], 'bc5'),
    'bfc6': bias_variable([4096], 'bfc6'),
    'bfc7': bias_variable([4096], 'bfc7'),
    'bfc8': bias_variable([4], 'bfc8')
  }
  return weights, biases

def inference(images, weights, biases, dropout):
  """Build the AlexNet model.

  Args:
    images: Images Tensor

  Returns:
    
  """
  # conv1
  conv1 = conv2d(images, weights['wc1'], [1, 4, 4, 1], biases['bc1'], 'conv1')
  print_activations(conv1)

  # pool1
  pool1 = max_pool(conv1, 'pool1')
  print_activations(pool1)

  # conv2
  conv2 = conv2d(pool1, weights['wc2'], [1, 1, 1, 1], biases['bc2'], 'conv2')
  print_activations(conv2)

  # pool2
  pool2 = max_pool(conv2, 'pool2')
  print_activations(pool2)

  # conv3
  conv3 = conv2d(pool2, weights['wc3'], [1, 1, 1, 1], biases['bc3'], 'conv3')
  print_activations(conv3)

  # conv4
  conv4 = conv2d(conv3, weights['wc4'], [1, 1, 1, 1], biases['bc4'], 'conv4')
  print_activations(conv4)

  # conv5
  conv5 = conv2d(conv4, weights['wc5'], [1, 1, 1, 1], biases['bc5'], 'conv5')
  print_activations(conv5)

  # pool5
  pool5 = max_pool(conv5, 'pool5')
  print_activations(pool5)

  # fc6
  pool5_flat = tf.reshape(pool5, [-1, weights['wfc6'].get_shape().as_list()[0]])
  print_activations(pool5_flat)
  fc6 = tf.nn.relu(tf.matmul(pool5_flat, weights['wfc6']) + biases['bfc6'], name='fc6')
  fc6 = tf.nn.dropout(fc6, dropout)
  print_activations(fc6)

  # fc7
  fc7 = tf.nn.relu(tf.matmul(fc6, weights['wfc7']) + biases['bfc7'], name='fc7')
  fc7 = tf.nn.dropout(fc7, dropout)
  print_activations(fc7)

  # fc8
  fc8 = tf.nn.relu(tf.matmul(fc7, weights['wfc8']) + biases['bfc8'], name='fc8')
  print_activations(fc8)

  return fc8

  
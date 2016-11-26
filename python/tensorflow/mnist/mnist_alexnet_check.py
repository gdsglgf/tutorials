# -*- coding: utf-8 -*-
import os
import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt

# 定义网络超参数
learning_rate = 0.001
training_iters = 200000
batch_size = 64
display_step = 20

# 定义网络参数
n_input = 784 # 输入的维度
n_classes = 10 # 标签的维度
dropout = 0.8 # Dropout 的概率

# 占位符输入
x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)

# 卷积操作
def conv2d(name, l_input, w, b):
    return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(l_input, w, strides=[1, 1, 1, 1], padding='SAME'),b), name=name)

# 最大下采样操作
def max_pool(name, l_input, k):
    return tf.nn.max_pool(l_input, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME', name=name)

# 归一化操作
def norm(name, l_input, lsize=4):
    return tf.nn.lrn(l_input, lsize, bias=1.0, alpha=0.001 / 9.0, beta=0.75, name=name)

# 定义整个网络 
def alex_net(_X, _weights, _biases, _dropout):
    # 向量转为矩阵
    _X = tf.reshape(_X, shape=[-1, 28, 28, 1])

    # 卷积层
    conv1 = conv2d('conv1', _X, _weights['wc1'], _biases['bc1'])
    # 下采样层
    pool1 = max_pool('pool1', conv1, k=2)
    # 归一化层
    norm1 = norm('norm1', pool1, lsize=4)
    # Dropout
    norm1 = tf.nn.dropout(norm1, _dropout)

    # 卷积
    conv2 = conv2d('conv2', norm1, _weights['wc2'], _biases['bc2'])
    # 下采样
    pool2 = max_pool('pool2', conv2, k=2)
    # 归一化
    norm2 = norm('norm2', pool2, lsize=4)
    # Dropout
    norm2 = tf.nn.dropout(norm2, _dropout)

    # 卷积
    conv3 = conv2d('conv3', norm2, _weights['wc3'], _biases['bc3'])
    # 下采样
    pool3 = max_pool('pool3', conv3, k=2)
    # 归一化
    norm3 = norm('norm3', pool3, lsize=4)
    # Dropout
    norm3 = tf.nn.dropout(norm3, _dropout)

    # 全连接层，先把特征图转为向量
    dense1 = tf.reshape(norm3, [-1, _weights['wd1'].get_shape().as_list()[0]]) 
    dense1 = tf.nn.relu(tf.matmul(dense1, _weights['wd1']) + _biases['bd1'], name='fc1') 
    # 全连接层
    dense2 = tf.nn.relu(tf.matmul(dense1, _weights['wd2']) + _biases['bd2'], name='fc2') # Relu activation

    # 网络输出层
    out = tf.matmul(dense2, _weights['out']) + _biases['out']
    return out

# 存储所有的网络参数
weights = {
    'wc1': tf.Variable(tf.zeros([3, 3, 1, 64])),
    'wc2': tf.Variable(tf.zeros([3, 3, 64, 128])),
    'wc3': tf.Variable(tf.zeros([3, 3, 128, 256])),
    'wd1': tf.Variable(tf.zeros([4*4*256, 1024])),
    'wd2': tf.Variable(tf.zeros([1024, 1024])),
    'out': tf.Variable(tf.zeros([1024, 10]))
}
biases = {
    'bc1': tf.Variable(tf.zeros([64])),
    'bc2': tf.Variable(tf.zeros([128])),
    'bc3': tf.Variable(tf.zeros([256])),
    'bd1': tf.Variable(tf.zeros([1024])),
    'bd2': tf.Variable(tf.zeros([1024])),
    'out': tf.Variable(tf.zeros([n_classes]))
}

# 构建模型
pred = alex_net(x, weights, biases, keep_prob)

data_dir = 'test/'
filenames = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.startswith('test')]
images = np.array([])
# print len(filenames)
for f in filenames:
    img = Image.open(f).resize((28, 28))
    image = np.array(img.convert('L'))
    # image = np.array(Image.open(f).convert('L'))
    image = image.astype(np.float32)
    image = np.multiply(image, 1.0 / 255.0)
    image = image.reshape(n_input)
    # print image.shape
    # print image
    images = np.append(images, image)

    # plt.imshow(image.reshape(28, 28), cmap='gray')
    # plt.show()

# print images.shape
images = images.reshape(-1, n_input)
print images.shape

model_dir = 'tmp/'
models = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if f.startswith('model') and not f.endswith('.meta')]
if len(models) > 0:
    models.sort(key = lambda x: int(x.split('-')[-1]))  # sort by global step
    print(models)
    for cp in models:
        saver = tf.train.Saver()
        with tf.Session() as sess:
            print('load model %s' %(cp))
            saver.restore(sess, cp)
            # print sess.run(biases['out'])
            output = sess.run(pred, feed_dict={x: images, keep_prob: 1.})

            rank = np.argsort(output)
            top1, top5 = [], []
            for input_im_ind in range(output.shape[0]):
                inds = rank[input_im_ind,:]
                fname = filenames[input_im_ind]
                label = int(fname.split('_')[1].split('.')[0])
                # print "Image", input_im_ind, fname, label
                if inds[-1] == label:
                    top1.append(fname)
                for i in range(5):
                    if inds[-1-i] == label:
                        top5.append(fname)
                    # print inds[-1-i], output[input_im_ind, inds[-1-i]]

            num_images = len(filenames)
            print('top1: %d/%d, top5: %d/%d' %(len(top1), num_images, len(top5), num_images))
            # print('filenames:')
            # print(filenames)
            # print('top1 matching:')
            # print(top1)
            # print('top5 matching:')
            # print(top5)

# saver = tf.train.Saver()
# with tf.Session() as sess:
#     checkpoint_dir = 'tmp/'
#     ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
#     if ckpt and ckpt.model_checkpoint_path:
#         print 'load model %s' %(ckpt.model_checkpoint_path)
#         saver.restore(sess, ckpt.model_checkpoint_path)
#     else:
#         print('No checkpoint file found at %s' % checkpoint_dir)
#     print sess.run(biases['out'])
#     output = sess.run(pred, feed_dict={x: images, keep_prob: 1.})

# # for i in range(output.shape[0]):
# #     print output[i]

# rank = np.argsort(output)
# for input_im_ind in range(output.shape[0]):
#     inds = rank[input_im_ind,:]
#     print "Image", input_im_ind, filenames[input_im_ind]
#     for i in range(5):
#         print inds[-1-i], output[input_im_ind, inds[-1-i]]

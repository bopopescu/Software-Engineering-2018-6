#!/etc/anaconda3/bin/python
import tensorflow as tf
import os
import numpy as np
from attr import Attr

# Setup the configuration for GPU
#os.environ['CUDA_VISIBLE_DEVICES'] = '0'
#config = tf.ConfigProto()
#config.gpu_options.per_process_gpu_memory_fraction = 0.19
#session = tf.Session(config=config)

def next_batch(num, data, labels):
	idx = np.arange(0, len(data))
	np.random.shuffle(idx)
	idx = idx[:num]
	data_shuffle = [data[i] for i in idx]
	labels_shuffle = [labels[i] for i in idx]
	return np.asarray(data_shuffle), np.asarray(labels_shuffle)

def build_CNN_classifier(x):
	x_image = x

	W_conv1 = tf.Variable(tf.truncated_normal(shape=[5,5,3,1], stddev=5e-2))
	b_conv1 = tf.Variable(tf.constant(0.1, shape=[1]))
	h_conv1 = tf.nn.relu(tf.nn.conv2d(x_image, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
	
	W_fc1 = tf.Variable(tf.truncated_normal(shape=[200 * 300 * 1, 1000], stddev=5e-2))
	b_fc1 = tf.Variable(tf.constant(0.1, shape=[1000]))
	
	h_conv1_flat = tf.reshape(h_conv1, [-1, 200 * 300 * 1])
	h_fc1 = tf.nn.relu(tf.matmul(h_conv1_flat, W_fc1) + b_fc1)
	h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

	W_fc2 = tf.Variable(tf.truncated_normal(shape=[1000, 1000], stddev=5e-2))
	b_fc2 = tf.Variable(tf.constant(0.1, shape=[1000]))
	logits = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
	y_pred = tf.nn.softmax(logits)

	return y_pred, logits


x = tf.placeholder(tf.float32, shape=[None, 200, 300, 3])
y = tf.placeholder(tf.float32, shape=[None, 1000])
keep_prob = tf.placeholder(tf.float32)

#pre.dataset = pre.dataset.batch(128)
#iterator = pre.dataset.make_one_shot_iterator()
#x_train, y_train = iterator.get_next()


with tf.Session() as sess:
	tmp = Attr()
	tmp.parsing()
	x_train = list()
	y_train = tmp.file_attr
	for item in tmp.file_name:
		with tf.gfile.FastGFile(item, 'rb') as f:
			image_data = f.read()
		decoded_image = tf.image.decode_jpeg(image_data, channels=3)
		resized_image = tf.image.resize_images(decoded_image, [200,300])
		image = sess.run(resized_image)
		x_train.append(image)

y_pred, logits = build_CNN_classifier(x)

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits))
train_step = tf.train.AdamOptimizer(1e-3).minimize(loss)

correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for i in range(10):
		batch = next_batch(128, x_train, y_train)
		train_accuracy = accuracy.eval(feed_dict={x:batch[0], y: batch[1], keep_prob: 1.0})
		loss_print = loss.eval(feed_dict={x: batch[0], y: batch[1], keep_prob: 1.0})
		print("epoch: %d, training data accuracy: %f, loss: %f" % (i, train_accuracy, loss_print))
		sess.run(train_step, feed_dict={x: batch[0], y: batch[1], keep_prob: 0.8})


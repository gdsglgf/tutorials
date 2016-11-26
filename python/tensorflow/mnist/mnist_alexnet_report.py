import numpy as np
import matplotlib.pyplot as plt

def read_report_data(csv):
	train = []
	validation = []

	with open(csv, 'r') as f:
		next(f)		# skip csv header title(step,loss,acc)
		last = -1
		for line in f:
			step, loss, acc = line.rstrip('\n').split(',')
			step = int(step)
			loss = float(loss)
			acc = float(acc)

			row = [step, loss, acc]
			if step == last:
				validation.append(row)
			else:
				train.append(row)

			last = step

	return train, validation

def extract_data(data):
	data = np.array(data)

	step = data[:, 0]
	loss = data[:, 1]
	acc = data[:, 2]

	return step, loss, acc

def test_extract_data():
	data = [[1, 2, 3], [4, 5, 6]]
	step, loss, acc = extract_data(data)
	print step
	print loss
	print acc

def plot_demo():
	x = np.arange(0, 5, 0.1);
	y = np.sin(x)
	plt.plot(x, y)
	plt.show()

def subplot_demo():
	# plot a line, implicitly creating a subplot(111)
	plt.plot([1,2,3])
	# now create a subplot which represents the top plot of a grid
	# with 2 rows and 1 column. Since this subplot will overlap the
	# first, the plot (and its axes) previously created, will be removed
	plt.subplot(211)
	plt.title('s1')
	plt.plot(range(12))
	plt.subplot(212, axisbg='y') # creates 2nd subplot with yellow background
	plt.title('s2')
	plt.show()

if __name__ == '__main__':
	# subplot_demo()

	train, validation = read_report_data('mnist_alexnet_train_report.csv')
	train_step, train_loss, train_acc = extract_data(train)

	plt.subplot(221)
	plt.title('loss')
	plt.xlabel('step')
	plt.ylabel('loss')
	plt.plot(train_step, train_loss)

	plt.subplot(222)
	plt.title('acc')
	plt.xlabel('step')
	plt.ylabel('acc')
	plt.plot(train_step, train_acc)

	step, loss, acc = extract_data(validation)
	plt.subplot(223)
	plt.title('loss')
	plt.xlabel('step')
	plt.ylabel('loss')
	plt.plot(step, loss)

	plt.subplot(224)
	plt.title('acc')
	plt.xlabel('step')
	plt.ylabel('acc')
	plt.plot(step, acc)

	plt.show()



def square(x):
	return x * x

l = [1, 2, 3, 4, 5]
print(map(square, l))				# [1, 4, 9, 16, 25]
print([x*x for x in range(1, 6)])	# [1, 4, 9, 16, 25]


def add(x,y):
	return x + y
print(reduce(add, [x*x for x in range(1, 6)]))	# 55
print(sum([x*x for x in range(1, 6)]))			# 55


def even(x):
	return (x >> 1) << 1 == x

print(filter(even, range(1, 10)))		# [2, 4, 6, 8]

print(type(range(1, 6)))		# <type 'list'>
import struct

value = 1234
fname = 'tmp'
with open(fname, 'wb') as f:
	if isinstance(value, int):
		print(bin(value))
		print(hex(value))
		f.write(struct.pack('i', value)) # write an int
	elif isinstance(value, str):
		f.write(value) # write a string
	else:
		raise TypeError('Can only write str or int')

	f.write(struct.pack('B', 12)) # write an unsigned char

with open(fname, 'rb') as f:
	my_number_back = struct.unpack('i', f.read(4))[0]
	print(my_number_back)
	print(struct.unpack('B', f.read(1))[0])
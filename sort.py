# change encoding to utf-8
import time
f = open('text.txt', 'r')
list = []

for i in f:
	a = i.split(';')
	if a[0] in list:
		print('This quote is already in the list')
	else:
		list.append(a[0])
		print('Add value to list - ' + a[0])
		z = open('kotir.txt', 'a')
		z.write(a[0] + '\n')
		z.close()

print("Things are good")

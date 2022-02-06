# change encoding to utf-8
f = open('text.txt', 'r')
list = []

for i in f:
	'''list.append(i)'''
	a = i.split(';')
	if a[0] in list:
		pass
	else:
		list.append(a[0])
		z = open('kotir.txt', 'a')
		z.write(a[0] + '\n')
		z.close()

print(list)

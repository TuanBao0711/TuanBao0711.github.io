n, m = map(int, input().split())
ma = []
xet = []
for i in range(n):
	lst = [int(x) for x in input().split()]
	ma.append(lst)
if n > m:
	for i in range(n):
		xet.append(i)
	chenhlech = n - m
	for i in range(0,chenhlech*2-1,2):
		xet[i]= -1
	for i in range(n):
		if xet[i] != -1:
			for j in range(m):
				print(ma[i][j], end = ' ')
			print()
elif m > n:
	for i in range(m):
		xet.append(i)
	chenhlech = m - n
	for i in range(1,chenhlech*2,2):
		xet[i]= -1
	for i in range(n):
		for j in range(m):
			if xet[j] != -1:
				print(ma[i][j], end = ' ')
		print()
else:
	for i in range(n):
		for j in range(m):
			print(ma[i][j], end = ' ')
		print()
'''
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7


2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9'''


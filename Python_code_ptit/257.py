import math
n, m = map(int, input().split())
ma = []
so  = -1
for i in range(n):
	lst = [int(x) for x in input().split()]
	ma.append(lst)
minn = ma[0][0]
maxx = -1
for i in range(n):
	for j in range(m):
		if ma[i][j] > maxx:
			maxx = ma[i][j]
		elif ma[i][j] < minn:
			minn = ma[i][j] 
kq = maxx - minn
xet = 0

for i in range(n):
	for j in range(m):
		if ma[i][j] == kq:
			xet+=1
			
if xet:
	print(kq)
	for i in range(n):
		for j in range(m):
			if ma[i][j] == kq:
				xet+=1
				print ("Vi tri [{}][{}]".format(i,j))

else:	print('NOT FOUND')

'''
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77

Vi tri [2][1]

Vi tri [3][3]
'''
import math
def snt(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n)+1)):
		if n % i == 0: return False
	return True
n, m = map(int, input().split())
ma = []
so  = -1
for i in range(n):
	lst = [int(x) for x in input().split()]
	ma.append(lst)
for i in range(n):
	for j in range(m):
		if snt(ma[i][j]) and ma[i][j] > so:
			so = ma[i][j]
if so == -1:
	print('NOT FOUND')
else:
	print(so)
	for i in range(n):
		for j in range(m):
			if ma[i][j] == so:
				print ("Vi tri [{}][{}]".format(i,j))

'''
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29

Vi tri [2][1]

Vi tri [3][0]

Vi tri [5][3]'''
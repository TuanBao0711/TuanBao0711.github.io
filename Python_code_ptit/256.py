import math
def thuannghich(n):
	a = str(n)
	if len(a) < 2: return False
	for i in range(len(a)):
		if a[i] != a[len(a)-1-i]: return False
	return True
n, m = map(int, input().split())
ma = []
so  = -1
for i in range(n):
	lst = [int(x) for x in input().split()]
	ma.append(lst)
for i in range(n):
	for j in range(m):
		if thuannghich(ma[i][j]) and ma[i][j] > so:
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
6 4

23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77

77

Vi tri [0][2]

Vi tri [3][1]

Vi tri [5][2]

Vi tri [5][3]'''
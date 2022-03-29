n = int(input())
ma = []
for i in range(n):
	ma.append([int(x) for x in input().split()])
lst = []
lst.append(int((ma[0][1]+ ma[0][2] - ma[1][2])/2))
for i in range(1,n):
	lst.append(ma[0][i] - lst[0])
for i in lst:
	print(i,end = ' ')

'''
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
'''
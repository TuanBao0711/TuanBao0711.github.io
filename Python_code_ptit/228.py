import math
def nto(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if not n%i: return False
	return True

n = int(input())
lst = [int(x) for x in input().split()]
lst1 = []
for i in range(n):
	if nto(lst[i]): 
		lst1.append(lst[i])
		lst[i] = -1
lst1.sort()
x = 0
for i in range(n):
	if lst[i] == -1:
		print(lst1[x],end = ' ')
		x+=1
	else: print(lst[i],end = ' ')



import math
def snt(n):
	if n < 2:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0: return False
	return True

n, x = map(int,input().split())
print(x, end = ' ')
lst = [x]
i = 2
while len(lst) <= n:
	if snt(i): 
		lst.append(i)
	i += 1
for i in range(1,n+1):
	lst[i] = lst[i]+lst[i-1]
	print(lst[i],end = ' ')

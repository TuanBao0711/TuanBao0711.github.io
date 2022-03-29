import math

def snt(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if not n%i: return False
	return True

def solve(n):
	count = 0
	for i in n:
		if snt(int(i)): count+=1
	if 2 * count > len(n): return True
	else: return False

t = int(input())
while t:
	so = input()
	if snt(len(so)) and solve(so): print("YES")
	else: print("NO")
	t-=1
import math

def snt(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if not n%i: return False
	return True

def solve(n):
	if snt(int(n[:3])) and snt(int(n[-3:])): return True
	else: return False

t = int(input())
while t :
	so = input()
	if solve(so):
		print("YES")
	else: print("NO")
	t-=1
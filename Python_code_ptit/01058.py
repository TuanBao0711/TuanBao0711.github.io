import math

def snt(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if not n%i: return False
	return True

def solve(n):
	so = int(n[-4:])
	if snt(so): print ("YES")
	else: print("NO")
t = int(input())
while t:
	str1 = input()
	solve(str1)
	t-=1
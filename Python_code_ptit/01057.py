import math

def snt(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if not n%i: return False
	return True

def solve (n):
	for i in range(len(n)):
		if snt(i):
			if n[i] != '7' and n[i] != '5' and n[i] != '3' and n[i] != '2':
				return False
		else:
			if n[i] == '7' or n[i] == '5' or n[i] == '3' or n[i] == '2':
				return False
	return True

t = int(input())
while t:
	n = input()
	if solve(n): print("YES")
	else: print("NO")
	t-=1
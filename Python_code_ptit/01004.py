import math

def snt(a):
	count = 0
	for i in range (1,a+1):
		if not a%i:
			count += 1
	if count != 2: return False
	else: return True

def solve(a, b):
		if a == b:
			return a 
		while(a!=b):
			if a>b:
				a-=b
			else:
				b-=a 
		return a
t = int(input())
while t:
	n = int(input())
	count = 0
	for i in range (1,n):
		if solve(i,n) == 1: count +=1
	if snt(count): print('YES')
	else: print('NO')
	t-=1
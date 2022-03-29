import math

def snt(n):
	if n < 2: return False
	for i in range(2,int(math.sqrt(n))+1):
		if not n%i: return False
	return True

def solve(n):
	lst =list(n)
	for i in range(len(n)):
		lst[i] = int(lst[i])
		if (i + lst[i]) % 2: return False
	return True

def solve1 (n):
	lst = map(int,list(n))
	return sum(lst)

t = int(input())
while t:
	n = input()
	if solve(n) and snt(solve1(n)): print ("YES")
	else : print ("NO")
	t-=1


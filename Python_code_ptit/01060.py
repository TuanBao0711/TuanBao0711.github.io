import math

def solve(n):
	lst = list(n)
	for i in range(len(n)):
		lst[i] = int(lst[i])
	s = 0
	for i in range(len(n)):
		if i % 2:
			s+= lst[i]
	return s 

def solve1(n):
	lst = list(n)
	for i in range(len(n)):
		lst[i] = int(lst[i])
	t=1
	for i in range(len(n)):
		if not i % 2 and lst[i] != 0:
			t *= lst[i]
	
	return t 

t = int(input())
while t:
	so = input()
	print("{} {}".format(solve1(so),solve(so)))
	t-=1
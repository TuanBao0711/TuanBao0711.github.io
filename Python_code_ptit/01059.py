import math

def solve(n):
	lst = list(n)
	for i in range(len(n)):
		lst[i] = int(lst[i])
	s = 0
	for i in range(len(n)):
		if i % 2 == 0:
			s+= lst[i]
	return s 

def kt(n):
	lst = list(n)
	s = 0
	for i in range(len(n)):
		if i % 2: s+= int(lst[i])
	if s:
		return True
	else: return False

def solve1(n):
	lst = list(n)
	t=1
	if kt(n):
		for i in range(len(n)):
			if i % 2 and lst[i] != '0':
				t *= int(lst[i])
	else: t = 0
	return t 

k = int(input())
while k:
	so = input()
	print("{} {}".format(solve(so),solve1(so)))
	k -= 1 
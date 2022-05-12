import math
import sys

def tongcs(n):
	t = 0
	for i in n:
		t += int(i)
	return t
def thuannghich(n):
	lst = []
	while n:
		lst.append(n%10)
		n//=10
	l = len(lst)
	if l < 2: return False
	else:
		for i in range(l):
			if lst[i] != lst[l-i-1]: return False
		return True

t = int(input())
while t:
	so = input()
	k = tongcs(so)
	if thuannghich(k): print("YES")
	else: print("NO")
	
	t-=1
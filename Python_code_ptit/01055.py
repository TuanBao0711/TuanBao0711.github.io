import math


def dk2(n):
	if len(n) % 2:
		for i in range (0,len(n)-1,2):
			if n[i] != n[i+2]: return False
	elif len(n) % 2 == 0: return False
	return True

t = int(input())
while t:
	n = input()
	if n[0] == n[1]:
		print ("NO")
	else:
		if dk2(n): print("YES")
		else: print ("NO")
	t-=1
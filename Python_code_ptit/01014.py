a, K, N = map(int,input().split())
lst = []
N -= a
a = (a // K + 1)* K -a
while a <= N:
	lst.append(str(a))
	a+=K
if len(lst):
	print(" ".join(lst))
else: print(-1)

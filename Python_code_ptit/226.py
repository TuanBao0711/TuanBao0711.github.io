def solve(a,b):
	if len(a) != len(b): return False
	else: 
		for i in range(len(a)):
			if a[i] != b[i]:
				return False
	return True

n, m = map(int,input().split())
lst = [int(i) for i in input().split()]
lst1 = [int(i) for i in input().split()]
a = []
b = []
for i in lst:
	if i not in a:
		a.append(i)
for i in lst1:
	if i not in b:
		b.append(i)
a.sort()
b.sort()
if solve(a,b): print("YES")
else: print("NO")
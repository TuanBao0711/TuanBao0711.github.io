import math
def snt(a):
	if a < 2: return False
	for i in range(2, int(math.sqrt(a))+1):
		if not a%i:
			return False
	return True

def solve(n):
	a,b = n,n
	count = 0
	while not snt(a) and not snt(b):
		a-=1
		b+=1
		count+=1
	return count

n = int (input())
lst = [int(x) for x in input().split()]
lst1 = []
for i in lst:
	lst1.append(solve(i))
print(max(lst1))
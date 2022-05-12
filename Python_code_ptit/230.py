import math
def snt(n):
	if n < 2: return False
	for i in range(2, int(math.sqrt(n))+1):
		if not n%i:
			return False
	return True

n = int(input())
lst1 = [int(x) for x in input().split()]
lst = []
for i in lst1:
	if i not in lst:
		lst.append(i)
kq = -1
s = 0
s1 =sum(lst)
for i in range(len(lst)):
	s += lst[i]
#	print("{} {}".format(s,s1-s))
	if snt(s) and snt(s1-s):
		kq = i
		break
if kq >= 0: print(kq)
else: print('NOT FOUND')
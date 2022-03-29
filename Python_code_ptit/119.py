P = 'abcdefghijklmnopqrstuvwxyz'
def solve(a,b):
	for i in range(len(a)-1):
		if abs(P.index(a[i]) - P.index(a[i+1])) != abs(P.index(b[i]) - P.index(b[i+1])): return False
	return True

		
t = int(input())
while t:
	str1 = input()
	k = list(str1)
	k.reverse()
	str2 = ''.join(k)
	if solve(str1,str2): print("YES")
	else: print("NO")
	t-=1

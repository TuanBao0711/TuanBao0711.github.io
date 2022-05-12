def UC(a,b):
	if a == b: return a 
	while a != b:
		if a > b: a -= b
		else: b -= a
	return a 

def rever(n):
	lst = list(n)
	lst.reverse()
	return ''.join(lst)

t = int(input())
while t:
	so = input()
	so1= int(rever(so))
	so = int(so)
	if UC(so,so1) == 1: print("YES")
	else: print("NO")
	t-=1
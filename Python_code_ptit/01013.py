def snt(a):
	if a < 2: return False
	else:
		count = 0;
		for i in range (1, a+1):
			if not a%i:
				count += 1
		if count == 2: return True
		else: return False

def UCLN(a, b):
	if a == b:
		return a 
	while a != b:
		if a > b: a-=b
		else: b -= a 
	return a 

def Tongcs(a):
	kq = 0;
	while a:
		kq += a%10
		a//=10
	return kq

t = int(input())
while t:
	str = input()
	lst = str.split()
	a = int(lst[0])
	b = int(lst[1])
	m = UCLN(a,b)
	n = Tongcs(m)
	if snt(n): print('YES')
	else: print('NO')
	t -= 1 
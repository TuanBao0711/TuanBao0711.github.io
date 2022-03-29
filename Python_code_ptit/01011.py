def chan(a):
	sum = 0
	while a:
		sum += a%10
		if sum % 2:
			return False
			break
		else: a//=10
	return True

def thuannghich(a):
	lst = list(a)
	lst.reverse()
	b = ''.join(lst)
	if b == a: return True
	else: return False 

def socs(a):
	if len(str(a)) % 2:
		return False
	else: return True

def solve (a):
	if chan(a) and thuannghich(str(a)) and socs(a):
		return True
	else: return False

t = int(input())
while t:
	a = int(input())
	str1 = ''
	for i in range (a):
		if solve(i):
			str1 += str(i) + ' '
	print(str1)
	t -= 1
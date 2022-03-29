import math
def snt(n):
	if n < 2: return False
	for i in range (2, int(math.sqrt(n))+1):
		if not n % i: return False
	return True
t = int(input())
while t:
	n = int(input())
	print ('1', end = ' ')
	for i in range(2, n+1):
		count = 0
		while not n % i and snt(i):
			count += 1
			m = n//i
			n//=i
		if count > 0: print ("* {}^{}".format(i,count), end = ' ')
	print()
	t-=1
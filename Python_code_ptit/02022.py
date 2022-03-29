
def nguyento(a):
	if a < 2: return False
	else:
		uoc = 1;
		for i in range (2,a+1):
			if not a % i:
				uoc += 1
		if uoc > 2: return False
		else: return True 
		
n = int(input())
lst = input().split()
lst1 = []
for i in range (1000):
	lst1.append(1)
for i in range (n):
	lst[i] = int(lst[i])

for i in lst:
	if lst1[i] and nguyento(i):
		print (i, " " , lst.count(i))
		lst1[i] = 0
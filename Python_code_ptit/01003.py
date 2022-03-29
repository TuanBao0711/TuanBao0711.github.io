t = int(input())
while t:
	str = input()
	lst = []
	for i in str:
		lst.append(int(i))
	n = len(str)
	for i in range (n-1,0,-1):
		if lst[i] == 0: continue
		if lst[i] >= 5:
			lst[i] = 0
			lst[i-1] += 1
		else: 
			if i != 1:
				lst[i] = 0
				lst[i-1] -= 1
			else:
				lst[i] = 0
	kq = 0
	for i in lst:
		kq = kq*10 + i
	print (kq)
	t-=1

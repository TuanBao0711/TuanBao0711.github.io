t = int(input())
k=t
while t:
	s1 = input()
	s2 = input()
	print ('Test {}:'.format(k-t+1), end = ' ')
	if len(s1) != len (s2): print("NO")
	else:
		lst1 = sorted(list(s1))
		lst2 = sorted(list(s2))

		kq = "YES"
		for i in range (len(s1)):
			if lst1[i] != lst2[i]:
				kq = 'NO'
				break
		print(kq)
	t-=1
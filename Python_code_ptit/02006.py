t = int(input())
while t:
	n = int(input())
	str1 = input()
	str2 = input()
	lst1 = str1.split()
	lst2 = str2.split()
	for i in range(n):
		lst1[i] = int(lst1[i])
		lst2[i] = int(lst2[i])

	lst1.sort()
	lst2.sort()

	kt = True
	for i in range (n):
		if lst1[i] > lst2[i]:
			kt = False
			break
	if kt:
		print ('YES')
	else:
		print('NO')
	t = t - 1
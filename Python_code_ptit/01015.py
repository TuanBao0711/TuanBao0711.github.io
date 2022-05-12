t = int(input())
for k in range (t):
	xet = True
	str1 = input()
	for i in range (len(str1)-1):
		if int(str1[i+1]) < int(str1[i]):
			xet = False
			break
	if xet:
		print ('YES')
	else:
		print('NO')
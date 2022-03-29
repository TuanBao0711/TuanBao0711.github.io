t = int(input())
while t:
	str = input()
	if int(str[:2]) == int(str[-2:]):
		print('YES')
	else:
		print ('NO')
	t = t-1
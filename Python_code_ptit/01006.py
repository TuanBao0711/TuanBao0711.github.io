t = int(input())
while t:
	str = input()
	xet = True
	for i in str:
		if int(i) != 4 and int(i) !=7:
			xet = False
			break
	if xet:
		print('YES')
	else: print('NO')
	t -=1 
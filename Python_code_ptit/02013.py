dk = True
while dk:
	n = int(input())
	if n <= 0:
		dk = False
		break
	else:
		count = 1
		while n != 1:
			if not n % 2:
				n /= 2
			else:
				n = n*3 + 1
			count += 1
		print (count)
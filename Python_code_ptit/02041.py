so1 = input()
so2 = input()
if len(so1) != len(so2):
	if len(so1) < len(so2):
		str1 = so1
		so1 = so2
		so2 = str1
	n2 = len(so2) 
	so = so1[-n2:]
	so3 = so1[:len(so1) - n2]
	tong = ''
	nho = 0
	for i in range (n2-1, -1, -1):
		kk = (int(so[i]) + int(so2[i]) + nho)
		if kk >= 10:
			kk %= 10
			nho = 1
		else: nho =0
		tong = str(kk) + tong
	if nho > 0:
		so3 = so3[:len(so3)-2] + str(int(so3[len(so3)-1])+1)
	kq = so3+tong
	print(kq.lstrip('0'))
else:
	n2 = len(so2) 
	tong = ''
	nho = 0
	for i in range (n2-1, -1, -1):
		kk = (int(so1[i]) + int(so2[i]) + nho)
		if kk >= 10:
			kk %= 10
			nho = 1
		else: nho =0
		tong = str(kk) + tong
	so3 = ''
	if nho > 0:
		so3 = str(1)
	kq = so3+tong
	print(kq.lstrip('0'))
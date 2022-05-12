p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
	str1 = input()
	if str1 == '0':
		break
	else:
		lst= str1.split()
		str2 = lst[1] 
		n = int(lst[0])
		str3 = ''
		for i in range (len(str2)):
			index = p.find(str2[i])
			index = (index + n)%28
			str3 = str3 + p[index]
		print(''.join(reversed(str3)))
	

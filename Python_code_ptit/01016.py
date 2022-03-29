t = int(input())
while t:
	str = input()
	str1 = ''
	str2 =''
	for i in range (len(str)):
		if i % 2:
			str1 = str1 + int(str[i])*str2
		else:
			str2 = str[i]
	print (str1)
	t = t - 1

str1 = input()
n = len(str1)
lst = []
while len(str1) > 3:
	str2 = ',' + str1[-3:]
	lst.append(str2)
	str1 = str1[:len(str1)-3]
lst.append(str1)
lst.reverse()
print(''.join(lst))
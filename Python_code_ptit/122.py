import math
str1 = input()
count = 0
while len(str1) > 1 :
	if str1[0] == '-':
		s = ord('-') - ord('0')
		str1 = str1[1:]
	else: s = 0 
	for i in str1:
		s+= int(i)
	str1 = str(s)
	count+=1
	
print(count)
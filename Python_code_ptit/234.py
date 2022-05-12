str1 = input()
if len(str1) % 2:
	str1 = str1[:len(str1)-1]

n = len(str1)
dic = {}
for i in range(0,n-1,2):
	m = int(str1[i:i+2])
	if m not in dic:
		dic[m] = 1 
	else: dic[m] +=1

for i in dic:
	print("{} {}".format(i, dic[i]))
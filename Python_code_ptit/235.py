str1 = input()
k = int(input())
if len(str1) % 2:
	str1 = str1[:len(str1)-1]

n = len(str1)
dic = {}
lst = []
for i in range(0,n-1,2):
	m = int(str1[i:i+2])
	if m not in dic:
		dic[m] = 1 
		lst.append(m)
	else: dic[m] +=1
lst.sort()
dk = 0
for i in lst:
	if dic[i] >= k:
		print("{} {}".format(i, dic[i]))
		dk +=1
if not dk:
	print('NOT FOUND')
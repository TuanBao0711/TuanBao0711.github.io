t = int(input())
while t:
	n = int(input())
	lst = [int(i) for i in input().split()]
	dic = {}
	for i in lst:
		if i not in dic:
			dic[i] = 1
		else: dic[i] += 1
	for i in dic:
		if dic[i] % 2: 
			print(i)
	t-=1
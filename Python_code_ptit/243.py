t = int(input())
while t:
	str1 = input()
	N = input()
	str1=str1.replace(N,'+')
	count=0
	for i in str1:
		if i == '+':
			count+=1
	print(count)
	t-=1
def Solve(n):
	lst = []
	count = 0
	while n:
		lst.append(n%10)
		n//=10
	for i in range(len(lst)-1):
		if lst[i] <= lst[i+1]:
			count+=1
	# if count > 1: return False
	# else: return True
	return count

t = int(input())
while t:
	n = int(input())
	# if Solve(n):
	# 	print('YES')
	# else: print('NO')
	print(Solve(n))
	t-=1
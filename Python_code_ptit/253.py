n = int(input())
mt = []
for i in range (n):
	lst = [int(x) for x in input().split()]
	mt.append(lst)
sum1 = 0
sum2 = 0
k = int(input())
for i in range (n):
	for j in range(n-i-1):
		sum1+=mt[i][j]
for i in range (n):
	for j in range(n-i,n):
		sum2+=mt[i][j]
if abs(sum1 -  sum2) <= k:
	print('YES')
else:
	print('NO')
print(abs(sum1-sum2))
'''for i in range (n):
	for j in range(n):
		print(mt[i][j], end = ' ')
	print()'''
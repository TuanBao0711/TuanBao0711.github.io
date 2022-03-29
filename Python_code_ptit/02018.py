n = int(input())

lst = [int(i) for i in input().split()]
maxx = max(lst)
lst1 = []
for i in range(1,maxx+2):
	lst1.append(i)
for i in lst1:
	if i not in lst:
		print(i)
		break

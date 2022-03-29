t = int(input())
lst = [float(x) for x in input().split()]
ma = max(lst)
mi = min(lst)
lst1 = []
for i in lst:
	if i != ma and i != mi:
		lst1.append(i)
print(round(sum(lst1)/len(lst1),2))
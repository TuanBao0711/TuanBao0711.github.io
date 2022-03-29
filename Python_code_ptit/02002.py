a = []
a.append(1)
a.append(1)
for i in range (2,94):
	a.append(a[i-1] + a[i-2])
t = int(input())
while t:
	m,n = map(int,(input()).split())
	lst = []
	for i in range (m-1, n):
		lst.append(str(a[i]))

	print (' '.join(lst))
	t -= 1
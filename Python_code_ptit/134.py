def swap(n,a, b):
	p = n[a]
	q = n[b]
	n[a] = q
	n[b] = p
	return n
so = input()
swap(so,2,3)
print(so)


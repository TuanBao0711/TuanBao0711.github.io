def xet1(s):
	lst = list(s)
	if lst.count(lst[0]) != len(lst) and lst.count('0') < len(lst) - 1:
		return True
	else:
		return False

# print(xet1(input()))
t = int(input())
while t:
	so = input()
	if not xet1(so):
		print('-1')
	else:
		n = len(so)
		lst = [int(x) for x in list(so)]
		i = n-2
		while i>=0 and lst[i] <= lst[i+1] :
			i-=1
		if i < 0:
			print('-1')
		else:
			dau = lst[:i]
			cuoi = lst[i+1:]
			core = lst[i]-1
			# print(dau, lst[i],cuoi)
			while core not in cuoi:
				core -=1
			ind = cuoi.index(core)
			temp = lst[i]
			lst[i] = cuoi[ind]
			cuoi[ind] = temp
			# print(dau, lst[i],cuoi)
			kq = ''
			for k in dau:
				kq+=str(k)
			kq+=str(lst[i])
			for k in cuoi:
				kq+=str(k)
			if kq[0] == '0':
				print('-1')
			else:
				print(kq)
	t-=1
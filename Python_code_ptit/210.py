while True:
	n = int(input())
	if n == 0: break
	lst=[]
	while len(lst) < n:
		k = [int(x) for x in input().split()]
		lst += k 
	ma = max(lst)
	mi = min(lst)
	if ma == mi: print("BANG NHAU")
	else: print("{} {}".format(mi,ma))
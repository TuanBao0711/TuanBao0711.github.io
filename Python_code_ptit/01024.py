def solve(str):
	n = len(str)
	for i in range (n-1):
		if abs(int(str[i]) - int(str[i+1])) != 2: 
			return False
			break
	return True

def solve1(str):
	lst = []
	for i in str:
		lst.append(int(i))
	if sum(lst) % 10: return False
	else: return True


t = int(input())
while t:
	str = input()
	if solve1(str) and solve(str):
		print ('YES')
	else: print('NO	')
	t -= 1
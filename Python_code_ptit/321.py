from operator import itemgetter 
t = int(input())
dic = {}
while t:
	ten = input().title()
	kq = [int(x) for x in input().split()]
	dic[ten] = kq
	t-=1
dic1 = sorted(dic.items(), key = lambda x : (x[0], x[1]))
print(dic1)

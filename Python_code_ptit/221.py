t= int(input())
while t:
	n , m ,k = map(int, input().split())
	a= [int(x) for x in input().split()]
	b= [int(x) for x in input().split()]
	c= [int(x) for x in input().split()]
	a.sort()
	b.sort()
	c.sort()
	x,y,z = 0,0,0
	intersection = []
	while x < n and y < m and z< k:
		if a[x] == b[y] and b[y] == c[z]:
			intersection.append(a[x])
			x,y,z = x+1,y+1,z+1
		elif a[x] < b[y]: x+=1
		elif b[y] < c[z]: y+=1
		else: z+=1
	if len(intersection):
		for i in intersection:
			print(i, end = ' ')
		print()
	else: print('NO')
	t-=1
				
'''
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120


3 5 4
1 5 5
3 4 5 5 10
5 5 10 20

3 3 3 
1 2 3
4 5 6
7 8 9

'''
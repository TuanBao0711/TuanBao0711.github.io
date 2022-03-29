import math
import sys

def tongcs(n):
	t = 0
	while n:
		t += n%10
		n //= 10
	return t 
def swap(list, a, b):
	list[a], list[b] = list[b], list[a]
	return list

t = int(input())
while t:
	n = int(input())
	lst = [int(x) for x in input().split()]
	lst1= []
	for i in lst:
		lst1.append(tongcs(i))

	for i in range (n-1):
		for j in range (i+1,n):
			if lst1[i] > lst1[j]:
				swap(lst1,i,j)
				swap(lst,i,j)
			elif lst1[i] == lst1[j] and lst[i] > lst[j]:
				swap(lst1,i,j)
				swap(lst,i,j)

	for i in lst:
		print(i, end = ' ')
	print()
	t-=1
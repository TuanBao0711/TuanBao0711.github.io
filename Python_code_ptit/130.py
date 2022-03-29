import math
def pow(a,b):
	if b == 1: return a 
	else:
		if b%2: return pow(a,b//2) * pow(a,b//2) *a 
		else : return pow(a,b//2) * pow(a,b//2)
def UC(a,b):
	if a == b: return a 
	while a != b:
		if a > b: a -= b
		else: b -= a
	return a 
n , k = map(int,input().split())
lst = []
for i in range (pow(10,k-1) , pow(10,k)):
	if UC(i,n) == 1:
		lst.append(i)
for i in range (len(lst)):
	
	if i % 10 == 9: print(lst[i])
	else: print(lst[i],end = ' ')
n , m = map(int, input().split())
lst = [int(i) for i in input().split()]
lst1 = [int(i) for i in input().split()]
a=[]
b=[]
for i in lst:
	if i not in a:
		a.append(i)
for i in lst1:
	if i not in b:
		b.append(i)
a.sort()
b.sort()
ab = []
ba = []
giao = []

for i in a:
	if i in b:
		print(i,end = ' ')
print()
for i in a:
	if i not in b:
		print(i,end = ' ')
print()
for i in b:
	if i not in a:
		print(i,end = ' ')

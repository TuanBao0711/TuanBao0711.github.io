n = int(input())
str = input()
lst = str.split()

count = 0

for i in range (n):
	for j in range (i,n):
		if int(lst[i]) > int(lst[j]):
			count = count + 1

print (count)
n = int(input())
str1 = input()
lst1 = str1.split()
lst = []
for i in lst1:
	lst.append(int(i))
count = 0
for i in range (n-1):
	if lst[i] != lst[i+1]:
		count += 1

print (count)
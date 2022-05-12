str = input()
n = len(str)
count = 0
for i in str:
	if i.isupper():
		count = count + 1
if count > n/2:
	print (str.upper())
else:
	print (str.lower())
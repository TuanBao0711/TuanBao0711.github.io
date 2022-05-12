str = input()
count = 0
for i in str:
	if int(i) == 4 or int(i) == 7:
		count = count + 1
if count == 7 or count == 4:
	print('YES')
else: print('NO')
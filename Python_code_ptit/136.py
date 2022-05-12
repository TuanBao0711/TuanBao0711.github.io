def le(n):
	s = 0
	for i in range (1,n+1,2):
		s+=1/i 
	return s 
def chan(n):
	s = 0
	for i in range (2,n+1,2):
		s+=1/i 
	return s 
t = int(input())
while t:
	a = int(input())
	if a % 2:
		str1 = str(round(le(a),6))
	else: str1 = str(round(chan(a),6))
	phay = str1.index('.')
	if (len(str1) < phay + 7):
		str1 += '0'*(phay+7-len(str1))
	print(str1)
	t-=1

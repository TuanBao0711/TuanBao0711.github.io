from decimal import Decimal
'''def pow(a,b):
	p = 1;
	for i in range (1,b+1):
		p *= a 
	return b

tiengoc, pcent, tienlai = map(decimal,input().split())
pcent  = 1 + pcent/100

print(pow(tiengoc,tienlai))

nam = 1
tyle = tienlai / tiengoc'''

a = input()
print(type(a))
a = Decimal(a)
print(type(a))


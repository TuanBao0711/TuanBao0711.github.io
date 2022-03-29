import math
l , r = map(int,input().split())
for x in range (l, r-1):
	for y in range (x+1, r):
		if math.gcd(x,y) == 1:
			for z in range(y+1, r+1):
				if math.gcd(y,z) == 1 and math.gcd(x,z) == 1:
					print("({}, {}, {})".format(x,y,z))
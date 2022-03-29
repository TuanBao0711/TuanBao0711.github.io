def se(n):
	for i in n:
		if i != '8' and i != '6':
			return False
	return True

def phatloc(n):
	for i in range (len(n)-2):
		if n[i] != '6':
			if n[i+1] != '6' and n[i+2] != '6':
				return False
	return True

n = input()

if se(n) and phatloc(n): print("YES")
else: print ("NO")
t = int(input())
while t:
	n = int(input())
	count = 0
	for i in range(1,n):
		# if n%(i+1) == 0 or n(i+1) == 0:
		for j in range(1,n):
			if (i+1) * (j+i/2) == n:
				count+=1
	print(count)
	t-=1


def solve(n):
    a=0
    t=1
    while (t*(t + 1)<2*n):
        m=(1.0*n-(t*(t+1))/2)/(t+1)
        if (m-int(m)==0.0):
            a+=1
        t=t+1
    return a
x=int(input())
for i in range(0,x):
    n = int(input())
    print(solve(n))
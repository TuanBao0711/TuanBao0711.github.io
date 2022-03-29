import math

def nextPrime(n):
    while True:
        n += 1
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                break
            else:
                return n
def primeProduce(a):
    num = 1
    count = 1
    while count <= a:
        num = nextPrime(num)
        yield num
        count += 1
#arr = []
txt = input()
s = [int(s) for s in txt.split()]
N, x = s
arr = [ele for ele in primeProduce(N)]
print(arr)
for i in range(N):
    print(x, end = " ")
    x += arr[i]


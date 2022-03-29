import math

def isPrime(n):
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
    return True

n = int(input())
txt = input()
arr = set(int(s) for s in txt.split() if s.isdigit())
print(arr)

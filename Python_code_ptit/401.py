from decimal import Decimal
import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __init__(p, x, y):
        p.x = x
        p.y = y

    def distance(self, p):
        x1 = (p.x - self.x) **2
        y1 = (p.y - self.y) **2
        str1 = str(round(math.sqrt(x1+y1),4))
        ind = str1.index('.')
        kq = str1 + (ind + 5 - len(str1)) * '0'
        return kq  

        
        

if __name__ == '__main__':
t = int(input())
while t > 0:
    arr = input().split()
    p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
    p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
    print(p1.distance(p2))
    t -= 1


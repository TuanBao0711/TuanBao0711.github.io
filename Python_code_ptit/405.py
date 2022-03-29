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
        str1 = str(round(math.sqrt(x1+y1),3))
        ind = str1.index('.')
        kq = str1 + (ind + 4 - len(str1)) * '0'
        return kq  

t = int(input())
while t:
    arr = [int (x) for x in input().split()]
    A = Point(Decimal(arr[0]),Decimal(arr[1]))
    B = Point(Decimal(arr[2]),Decimal(arr[3]))
    C = Point(Decimal(arr[4]),Decimal(arr[5]))      
    AB = A.distance(B)
    BC = B.distance(C)
    AC = C.distance(A)

    if float(AB) + float(BC) > float(AC) and float(BC) + float(AC) > float(AB) and float(AB) + float(AC) > float(BC):
        print(round((float(AB) + float(BC) + float(AC)),3))
    else:
        print("INVALID")
    t-=1

#######################################

# def distance(x1,y1,x2, y2):
#     x = (x1 - x2) **2
#     y = (y1 - y2) **2
#     str1 = str(round(math.sqrt(x+y),3))
#     ind = str1.index('.')
#     kq = str1 + (ind + 4 - len(str1)) * '0'
#     return kq  
            

# t = int(input())
# while t:
#     arr = [int (x) for x in input().split()]     
#     AB = distance(Decimal(arr[0]),Decimal(arr[1]),Decimal(arr[2]),Decimal(arr[3]))
#     BC = distance(Decimal(arr[2]),Decimal(arr[3]),Decimal(arr[4]),Decimal(arr[5]))
#     AC = distance(Decimal(arr[4]),Decimal(arr[5]),Decimal(arr[0]),Decimal(arr[1]))

#     if float(AB) + float(BC) > float(AC) and float(BC) + float(AC) > float(AB) and float(AB) + float(AC) > float(BC):
#         print(round((float(AB) + float(BC) + float(AC)),3))
#     else:
#         print("INVALID")
#     t-=1
            


##################################

class Triangle(object):
    """docstring for Triangle"""
    def __init__(self, *arg):
        self.A = [Decimal(arg[0]),Decimal(arg[1])]
        self.B = [Decimal(arg[2]),Decimal(arg[3])]
        self.C = [Decimal(arg[4]),Decimal(arg[5])]

arr = [int (x) for x in input().split()]
trip1 = Triangle(arr)
print(trip1.A)


'''
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
'''
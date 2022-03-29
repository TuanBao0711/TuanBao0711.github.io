def xetdau(a):
    if a> 0: return '+ ' +str(a)
    else :return '- ' +str(-a) 

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __init__(p, x, y):
        p.x = x
        p.y = y
    def nhan(self, p):
        thuc = self.x * p.x -(self.y * p.y)
        ao = self.x * p.y + self.y * p.x
        self.x = thuc
        self.y = ao 
    def cong(self, p):
        thuc = self.x + p.x
        ao = self.y+p.y 
        self.x = thuc
        self.y = ao 
t = int(input())
lstkq = []
while t:
    lst = [int(x) for x in input().split()]
    A = Point(lst[0], lst[1])
    B = Point(lst[2], lst[3])
    A1 = Point(lst[0], lst[1])
    A.cong(B)
    A1.nhan(A)
    A.nhan(A)
    lstkq.append('{} {}i, {} {}i'.format(A1.x, xetdau(A1.y), A.x, xetdau(A.y)))
    t-=1
print(*lstkq, sep = '\n')

'''
3
1 2 3 4
2 3 4 5
1 -2 5 -6
'''
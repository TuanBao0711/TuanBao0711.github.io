import math
class SinhVien:
    def __init__(self,name,a,id):
        self.name = name
        self.a = [float(x) for x in a.split()]
        self.id='HS%02d'%id
        self.xh=""
        self.tb=0
    def trungbinh(self):
        sum=0
        dem=0
        for i in self.a:
            if dem<=1: sum+=(i*2.0) 
            else: sum+=i
            dem+=1
        self.tb=round(sum/10/1.2,1)
    def xephang(self):
        if self.tb>=9: self.xh="XUAT SAC"
        elif self.tb>=8: self.xh="GIOI"
        elif self.tb>=7: self.xh= "KHA"
        elif self.tb>=5: self.xh= "TB"
        else: self.xh= "YEU"
    def __str__(self):
        return self.id+' '+ self.name+' '+('%.1f'%self.tb)+' '+self.xh
lst=[]
for i in range(int(input())):
    lst.append(SinhVien(input(),input(),i+1))
for i in lst:
    i.trungbinh()
    i.xephang()
lstkq = sorted(lst, key = lambda x: x.tb, reverse=True)
for i in lstkq:
    print(i)
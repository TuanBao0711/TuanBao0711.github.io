from decimal import Decimal 
def xet(n):
  if n >= 108: return 'XUAT SAC'
  elif n >= 96: return 'GIOI'
  elif n >= 84: return 'KHA'
  elif n >= 60: return 'TB'
  else:  return 'YEU'

def maso(n):
  if len(str(n)) < 2: return '0'+str(n)
  else: return str(n)

class Diem(object):
  
  def __init__(self, ten, arg, ma):
    self.ten = ten
    self.tongdiem = sum(arg)
    self.diem = round((self.tongdiem/10/1.2),1)
    self.msv = 'HS' + maso(ma)
    self.xeploai = xet(self.tongdiem)

t = int(input())
stt= 1
lstsv = []
while stt <= t :
  ten = input()
  lstdiem = [(float(x))for x in input().split()]
  lstdiem.extend([lstdiem[0],lstdiem[1]])
  lstsv.append(Diem(ten, lstdiem, stt))
  stt+=1
lst = sorted(lstsv, key = lambda CD : (CD.tongdiem), reverse = True)
for i in lst:
  print('{} {} {} {}'.format(i.msv, i.ten, i.diem, i.xeploai))
  


# lstdiem = [Decimal(float(x))for x in input().split()]
# lstdiem.append(lstdiem[0])
# lstdiem.append(lstdiem[1])
# print(round(sum(lstdiem)/len(lstdiem),1))







'''
4
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.1  9.0  7.9  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Than Tuan Bao
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
'''
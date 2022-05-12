mon_hoc = {'A': 'TOAN', 'B':'LY' , 'C':'HOA'}
diem_uu_tien = {'1':2.0 , '2': 1.5, '3': 1.0 , '4':0.0}

def mon(a):
	return mon_hoc[a[0]]

def diemut(a):
	return diem_uu_tien[a[1]]

def kq(a):
	if a >= 18: return 'TRUNG TUYEN'
	else: return 'LOAI'

class GV(object):
 	"""docstring for GV"""
 	def __init__(self, ma,mamon, ten, tin, cm ):
 		self.ma  = 'GV%02d'%ma
 		
 		self.ten = ten 
 		self.diem = tin * 2 + cm + diemut(mamon)
 		self.monhoc = mon(mamon)  
 		self.kq = kq(self.diem) 

t = int(input())
stt = 1
lst = []
while stt <= t:
	ten = input()
	mamon = input()
	tin = float(input())
	cm = float(input())
	lst.append(GV(stt, mamon, ten, tin, cm))
	stt+=1
lst = sorted(lst, key = lambda i: i.diem, reverse = True)
for i in lst:
	print('{} {} {} {} {}'.format(i.ma, i.ten, i.monhoc, i.diem, i.kq))


'''
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
'''
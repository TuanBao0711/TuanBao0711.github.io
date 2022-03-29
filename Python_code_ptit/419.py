def xeploai(n):
	x = ''
	if n > 9.5: x = 'XUAT SAC'
	elif n >= 8: x = 'DAT' 
	elif n >= 5: x = 'CAN NHAC'
	else: x = 'TRUOT'
	return x

def diem(n):
	if n[0] == '0' or float(n) > 10:
		return float(n)/10
	else: return float(n)

class Thi_sinh(object):
	def __init__(self, ma, ten, lt, th):
		self.ma = 'TS%2d'%ma
		self.ten = ten.title()
		self.diem = (diem(lt) + diem(th))/2
		self.kq = xeploai(self.diem)

t = int(input())
stt = 1
lst = []
while stt <= t:
	ten = input()
	lt = (input())
	th = (input())
	lst.append(Thi_sinh(stt, ten, lt, th))
	stt+=1
lst = sorted(lst, key = lambda i: i.diem , reverse = True)
for i in lst:
	print('{} {} {} {}'.format(i.ma, i.ten, '%.2f'%i.diem, i.kq))		
'''
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''
def ngaypthang(thang , nam):
	if nam % 4 == 0 and thang == 2: return 29
	elif nam%4 != 0 and thang == 2: return 28
	elif thang in [1,3,5,7,8,10, 12]: return 31
	else : return 30

def songaycuanam(thang, nam):
	a = 0
	for i in range(1,thang):
		a+= ngaypthang(i, nam)
	return a 

def songay(dau, cuoi):
	den = [int(x) for x in dau.split('/')]
	ve  = [int(x) for x in cuoi.split('/')]
	come = den[2] * 365 + songaycuanam(den[1], den[2]) + den[0] + (den[2]-1)//4
	out = ve[2] * 365 + songaycuanam(ve[1], ve[2]) + ve[0] + (ve[2]-1)//4
	return out - come + 1

def don_gia(n):
	if str(n)[0] == '1': return 25
	elif str(n)[0] == '2': return 34
	elif str(n)[0] == "3": return 50
	else : return 80
# print(songaycuanam(9, 2020))


class Thue_phong(object):
	"""docstring for Thue_phong"""
	def __init__(self, ma, ten, sophong,den, ve, phuphi):
		self.ma = 'KH%02d'%ma
		self.ten = ten
		self.sophong = sophong
		self.ngaythue = songay(den, ve)
		self.dongiacanhan = don_gia(sophong) 
		self.tien = self.dongiacanhan*self.ngaythue + phuphi 
t = int(input())
stt = 1
lst = []
while stt <= t:
	ten = input()
	sophong = int(input())
	den = input()
	di = input()
	phuphi = int(input())
	lst.append(Thue_phong(stt, ten, sophong, den, di, phuphi))
	stt+=1
lst = sorted(lst, key = lambda x: x.tien, reverse = True)
for i in lst:
	print('{} {} {} {} {}'.format(i.ma, i.ten, i.sophong, i.ngaythue, i.tien))


# den = input()
# ve = input()
# phong = int(input())
# print(don_gia(phong))
# print(songay(den, ve))

'''
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
'''
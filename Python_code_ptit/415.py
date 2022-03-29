def phuphi(n):
	if n > 100: return 1.05
	elif n > 50: return 1.03
	else : return 1.02
def ma(n):
	if n < 10: return 'KH0' + str(n)
	else: return 'KH' + str(n)

def chi_so(cs):
	
	lst = [0,0,0]
	if cs <= 50:
		lst[0] = cs 
	elif cs <= 100:
		lst[0] = 50
		lst[1] = cs - 50
	else :
		lst[0] = 50
		lst[1] = 50
		lst[2] = cs - 100
	return lst

class KH(object):
	"""docstring for KH"""
	def __init__(self, ma, ten, chs):
		self.ma = ma
		self.ten = ten
		self.phuphi = phuphi(chs)
		self.tien = int(round((chi_so(chs)[0] * 100 + chi_so(chs)[1] * 150 + chi_so(chs)[2] * 200) * self.phuphi))
		

t = int(input())
stt = 1
lst = [] 
while stt<= t:
	makh = ma(stt)
	ten = input()
	cu = int(input())
	moi = int(input())
	chs = moi - cu
	lst.append(KH(makh, ten, chs))
	stt+=1
	lst = sorted(lst, key = lambda i: i.tien, reverse = True )
for i in lst:
	print('{} {} {}'.format(i.ma, i.ten, i.tien))

'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''
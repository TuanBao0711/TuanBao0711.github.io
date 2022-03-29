def tgian(ts, te):
	timestart = [int(x) for x in ts.split(':')]
	timesend = [int(x) for x in te.split(':')]
	return (-timestart[0]*60 - timestart[1] + timesend[0]*60 + timesend[1]) 

class Taikhoan(object):
	"""docstring for Taikhoan"""
	def __init__(self, ma, ten, arg):
		self.ma = ma
		self.ten = ten
		self.tong = arg
		self.gio = arg//60
		self.phut = arg%60

t = int(input())
lst = []
while t:
	ma = input()
	ten = input()
	bd = input()
	kt = input()
	time = tgian(bd, kt)
	lst.append(Taikhoan(ma, ten, time))
	t-=1
lst1 = sorted(lst, key = lambda i: i.tong, reverse = True)
for i in lst1:
	print('{} {} {} gio {} phut'.format(i.ma, i.ten, i.gio, i.phut))
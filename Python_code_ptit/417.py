def tgian(ts, te):
	timestart = [int(x) for x in ts.split(':')]
	timesend = [int(x) for x in te.split(':')]
	return (-timestart[0]*60 - timestart[1] + timesend[0]*60 + timesend[1])/60 
def ma(ten, dc):

	lst = dc.split()
	l = ten.split()
	lst+=l
	maa = ''
	for i in lst:
		maa+=i[0].upper()
	return maa

def vantoc(time):
	return round(120/time)

class Taydua(object):
	"""docstring for Taydua"""
	def __init__(self, ten,dc, time):
		self.ma = ma(ten,dc)
		self.dc = dc
		self.ten = ten 
		self.time = tgian( '6:00', time )
		self.vantoc = vantoc(self.time)

t= int(input())
lst = []
while t:
	ten = input()
	dc = input()
	tg = input()
	lst.append(Taydua(ten, dc, tg))
	t -=1

lst1 = sorted(lst, key = lambda i: i.time)
for i in lst1:
	print('{} {} {} {} Km/h'.format(i.ma, i.ten, i.dc, i.vantoc))
		

'''
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
'''
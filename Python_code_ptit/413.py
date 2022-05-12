def tgian(ts, te):
	timestart = [int(x) for x in ts.split(':')]
	timesend = [int(x) for x in te.split(':')]
	return (-timestart[0]*60 - timestart[1] + timesend[0]*60 + timesend[1]) 

def maso(n):
  if len(str(n)) < 2: return 'T0'+str(n)
  else: return 'T'+str(n)

class Domua(object):

	def __init__(self,ma, ten, time, luongmua):
		self.ten = ten		
		self.time = time 
		self.luongmua = luongmua
		self.ma = ma
		self.luongmuaph = round(self.luongmua/self.time * 60,2)


t = int(input())
stt=1
lst = []
lstten = []
while stt<=t:
	ma = maso(stt)
	ten = input()
	t1 = input()
	t2 = input()
	luongmua = int(input())
	time = tgian(t1, t2)
	if ten not in lstten:
		lstten.append(ten) 
		lst.append(Domua( ma,ten, time, luongmua))
	
	else:
		for i in lst:
			if ten == i.ten:
				time +=i.time
				luongmua += i.luongmua
				ma = i.ma
				lst.remove(i)
				lst.append(Domua(ma,ten, time, luongmua))
				break
	
	stt+=1
	
	lstkq = sorted(lst, key = lambda i : i.ma)
	

for i in lstkq:
	str1 = str(i.luongmuaph)
	ind = str1.index('.')
	kq = str1 + (ind + 3 - len(str1)) * '0'
	print('{} {} {}'.format(i.ma, i.ten,kq))
# for i in lst:
# 	print(i.__dict__)


'''
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
'''
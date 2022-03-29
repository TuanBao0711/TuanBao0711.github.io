def diem(s):
	diemcc = 10
	for i in s:
		if i == 'x': diemcc -= 0
		elif i == 'm': diemcc -= 1
		else: diemcc -= 2
	if diemcc < 0: diemcc =0
	return diemcc

def dieu_kien_thi(diemcc):
	if diemcc == 0: return 'KDDK'
	else: return ''

def diem_tuong_ung(dic, masv):
	return dic[masv]

class SV(object):
	"""docstring for SV"""
	def __init__(self,masv, ten, lop):
		self.masv = masv
		self.ten = ten
		self.lop = lop
		# self.diemcc = diem_tuong_ung[masv]
		# self.stt = dieu_kien_thi(self.diemcc)
lst = []
dic_diem = {}
t = int(input())
n = t
while t:
	masv = input()
	ten = input()
	lop = input()
	lst.append(SV(masv, ten, lop))
	t-=1
# for i in lst:
# 	print(i.__dict__)
while n:
	ma, diemdanh = [x for x in input().split()]
	dic_diem[ma] = diem(diemdanh)
	n-=1
# dic_diem = dict(sorted(dic_diem.items(), key = lambda x: x[1])) 
# print(dic_diem)
for sv in lst:
	for i in dic_diem:
		if sv.masv == i:
			print('{} {} {} {} {}'.format(sv.masv, sv.ten, sv.lop, dic_diem[i], dieu_kien_thi(dic_diem[i])))
'''
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
'''
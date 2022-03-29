import math
def tinh_toan(n):
	return n/(math.sqrt(2) + math.sqrt(6) + 2)
class Hinhvuong(object):
	"""docstring for Hinhvuong"""
	def __init__(self, dientich):
		self.canh = math.sqrt(dientich)
		self.bankinh = tinh_toan(self.canh)

dientich = float(input())
Square1 = Hinhvuong(dientich)
print('%.4f'%Square1.bankinh)
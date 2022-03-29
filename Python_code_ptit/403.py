import math

class Phanso(object):
	"""docstring for Phanso"""
	def __init__(self, *arg):
		self.tu, self.mau = arg[0],arg[1]
		self.gcd = math.gcd(self.tu,self.mau)
	def toigian(self):
		self.tu /= self.gcd
		self.mau /= self.gcd

tm = [int(x) for x in input().split()]
ps1  = Phanso(tm[0], tm[1])
ps1.toigian()
print("{}/{}".format(int(ps1.tu),int(ps1.mau)))		
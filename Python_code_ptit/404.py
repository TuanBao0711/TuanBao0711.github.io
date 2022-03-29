import math
class Phanso(object):
	"""docstring for Phanso"""
	def __init__(self, *arg):
		self.tu, self.mau = arg[0],arg[1]
		self.gcd = int(math.gcd(self.mau,self.tu))
	def __init__(Ps,*arg):
		Ps.tu, Ps.mau = arg[0],arg[1]
		Ps.gcd = int(math.gcd(Ps.mau,Ps.tu))
	def Ketqua(self,Ps):
		# self.tu = int(self.tu / self.gcd)
		# self.mau = int((self.mau) / self.gcd)
		# Ps.tu =int(Ps.tu / Ps.gcd)
		# Ps.mau = int (Ps.mau / Ps.gcd)
		tu = self.tu * Ps.mau + self.mau * Ps.tu
		mau = self.mau * Ps.mau
		chia = math.gcd(tu,mau)
		tu = int(tu/chia)
		mau = int(mau/chia)
		print("{}/{}".format(tu,mau))

inp = [int(x) for x in input().split()]
Phanso1= Phanso(inp[0],inp[1])
Phanso2 = Phanso(inp[2],inp[3])
Phanso1.Ketqua(Phanso2)
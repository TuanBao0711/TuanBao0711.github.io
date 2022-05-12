class TS(object):
	"""docstring for TS"""
	def __init__(self, Ten, ns, d1, d2,d3):
		self.Ten = Ten
		self.ns = ns
		self.d1 = d1
		self.d3 = d3
		self.d2 = d2

TS1 = TS(input(),input(),float(input()),float(input()),float(input()))
print("{} {} {}".format(TS1.Ten, TS1.ns,(TS1.d1+TS1.d2+TS1.d3)))


'''
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
'''
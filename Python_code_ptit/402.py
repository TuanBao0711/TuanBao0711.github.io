class Rectangle(object):
	"""docstring for Retangle"""
	def __init__(self, x,y,z):
		self.chuvi = (x+y)*2
		self.dientich = x * y
		self.color = z[:1].upper() + z[1:].lower()
if __name__ == '__main__':
	t = int(input())
	while t > 0:
	    arr = input().split()
	    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
	    print('{} {} {}'.format(r.chuvi, r.dientich, r.color))
	    t -= 1
		
		
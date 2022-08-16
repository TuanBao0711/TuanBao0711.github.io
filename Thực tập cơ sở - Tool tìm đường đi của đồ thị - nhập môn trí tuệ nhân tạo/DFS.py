import collections
data = collections.defaultdict(list)

data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K','L','M']
data['H'] = ['N','O']

class Node:
	def __init__(self, name, w = 0, par = None):
		self.name = name 
		self.par = par
		self.w = w 

	def display(self):
		print(self.name, self.par)

	def __lt__(self, other):
		return self.w < other.w 

def equal (O, G):
	return O.name == G.name

def check(tmp, Open):
	for x in Open:
		if equal(x, tmp):
			return True
	return False

def path(O, lst):
	lst.append(O.name)
	# print(O.name)
	if O.par != None:
		path(O.par, lst)
	else: 
		return

def DFS(start, goal ):
	S = Node(name = start)
	G = Node(name = goal)
	result_str = ''
	road = []
	# S =  Node(name = start)
 	# G =  Node(name = goal)
	Open = []
	Close = []
	Open.append(S)
	while True:
		if len(Open) == 0:
			result_str = 'Tìm kiếm thất bại'
			break
		O = Open.pop(0)
		Close.append(O)
		result_str += f'Duyệt {O.name}\n'
		if equal(O, G):
			result_str += 'Tìm kiếm thành công\n'
			path(O, road)
			for node in road:
				if node == 'A':
				    result_str += 'A\n'
				    # print("S")
				else:
				    result_str += "{} <- ".format(node)
			break
		pos = 0
		for x in data[O.name]:
			tmp = Node(x)
			tmp.par = O
			check1 = check(tmp, Open)
			check2 = check(tmp, Close)
			if not check1 and not check2:
				Open.insert(pos, tmp)
				pos +=1
	print(result_str)

DFS('A', 'M')
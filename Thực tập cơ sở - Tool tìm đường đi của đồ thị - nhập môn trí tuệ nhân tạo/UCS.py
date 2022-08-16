import collections
import queue 

data = collections.defaultdict(list)

#Cấu trúc mỗi cặp thể hiện điểm Kề cost tới điểm kề đó, giá trị cuối cùng là heuristic của điểm 
data['S'] = ['B', 2, 'C', 1, 'D',3]
data['B'] = ['E', 5, 'F', 4]
data['C'] = ['G', 6, 'H', 3]
data['D'] = ['I', 2, 'J', 4]
data['F'] = ['K', 1,'L', 1, 'M',4]
data['H'] = ['N',2, 'O',4]


class  Node:
    def __init__(self, name, par = None, g = 0, h = 0):
        self.name = name
        self.par = par
        self.g = g
    def display(self):
        print(self.name , self.g)
    def __lt__(self, other):
        if other == None:
            return False
        return self.g < other.g 
    def __eq__ (self, other): 
        if other == None:
            return False
        return self.name == other.name

def equal(A, B): 
    if A.name == B.name:
        return True
    return False
def CheckInQueue(tmp , c): 
    if tmp == None:
        return False
    return (tmp in c.queue)
def get_path(O, lst):
    lst.append(O.name)
    # print(O.name)
    if O.par != None:
        get_path(O.par, lst)
    else: 
        return

def UCS(start, goal):
    S = Node(name = start)
    G = Node(name = goal)
    road = []
    result_str = ''
    Open = queue.PriorityQueue()
    Close = queue.PriorityQueue()
    Open.put(S)
    while True:
        if Open.empty():    
            result_str += 'Tìm kiếm thất bại!'
            break
        O = Open.get()
        if CheckInQueue(O, Close):
            continue     
        Close.put(O)        
        # print('Duyet {} {}'.format(O.name, O.g))
        result_str += 'Duyet {} {} \n'.format(O.name, O.g)
        if equal(O, G):
            # print('Tìm kiếm thành công')
            result_str += 'Tìm kiếm thành công\n'
            get_path(O, road)                     
            # print('Khoảng cách: {}'.format(O.h+O.g))    
            for node in road:
                if node == S.name:
                    result_str += f'{S.name}\n'
                    # print("S")
                else:
                    result_str += "{} <- ".format(node)
            result_str += 'Khoảng cách: {}\n'.format(O.g)
            break
        i = 0
        while i< len(data[O.name]) -1:      #Duyệt theo thuật toán ưu tiên f(x) 
            name = data[O.name][i]
            g = O.g + data[O.name][i+1]
            tmp =  Node(name = name, g = g)
            tmp.par = O
            kks1 = False
            kks2 = CheckInQueue(tmp, Close)
            if not kks1 and not kks2:
                Open.put(tmp)
            i+=2
    print(result_str)
UCS('S', 'N')
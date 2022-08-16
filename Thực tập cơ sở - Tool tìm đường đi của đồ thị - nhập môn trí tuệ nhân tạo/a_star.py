import collections
import queue 

data = collections.defaultdict(list)

#Cấu trúc mỗi cặp thể hiện điểm Kề cost tới điểm kề đó, giá trị cuối cùng là heuristic của điểm 
data['S'] = ['B', 3, 'A', 2, 6]

data['A'] = ['C', 3, 4]
data['B'] = ['C', 1, 'D', 3, 4]
data['C'] = ['D', 1, 'E', 3, 4]
data['D'] = ['F', 2, 3]
data['E'] = ['G', 2, 1]
data['F'] = ['G', 1, 1]
data['G'] = [0]


class  Node:
    def __init__(self, name, par = None, g = 0, h = 0):
        self.name = name
        self.par = par
        self.g = g
        self.h = h 
    def display(self):
        print(self.name , self.g, self.h)
    def __lt__(self, other):#Hàm để so sánh dựa theo "f = g + h" khi cho vào queue
        if other == None:
            return False
        return self.g + self.h < other.g + other.h
    def __eq__ (self, other): #Hàm so sánh 2 đối tượng dựa theo tên
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
def get_path(A, road): #Đệ quy đường đi
    print(A.name)
    road+= A.name
    if A.par != None:
        get_path(A.par, road)
    else: return


def A_star(start , goal):
    result = ''
    S=  Node(name = start)
    G =  Node(name = goal)
    Open = queue.PriorityQueue()
    Close = queue.PriorityQueue()
    S.h = data[S.name][-1] #Lấy chỉ số heuristic
    Open.put(S)             # Đẩy S vào hàng đợi
    while True:
        if Open.empty():    #Hàng đợi trống và kết thúc với ko có đường đi
            print('Tìm kiếm thất bại!')
            result += 'Tìm kiếm thất bại!'
            break
        O = Open.get()      #Lấy phần tử được ưu tiên nhất
        if CheckInQueue(O, Close):
            continue
        Close.put(O)        
        print('Duyet {} {} {}'.format(O.name, O.g, O.h))
        result += 'Duyet {} {} {} \n'.format(O.name, O.g, O.h)
        if equal(O, G):
            print('Tìm kiếm thành công')
            result += 'Tìm kiếm thành công\n'
            get_path(O, result)                     #Suy ra đường đi khi đến đích
            print('Khoảng cách: {}'.format(O.h+O.g))    
            result += 'Khoảng cách: {}\n'.format(O.h+O.g)
            break
        i= 0
        while i< len(data[O.name]) -1:      #Duyệt theo thuật toán ưu tiên f(x) 
            name = data[O.name][i]
            g = O.g + data[O.name][i+1]
            h = data[name][-1]
            tmp =  Node(name = name, g = g, h=h)
            tmp.par = O

            kks1 = False
            kks2 = CheckInQueue(tmp, Close)
            if not kks1 and not kks2:
                Open.put(tmp)
            i+=2
    # print(result)

# A_star( Node('S'),  Node('G'))
A_star( 'S',  'G') #Chạy hàm

import collections
import queue 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


#----------------------------


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
def get_path(A,lst): #Đệ quy đường đi
    lst.append(A.name)
    if A.par != None:
        get_path(A.par, lst)
    else: return

class Ui_MainWindow(object):
    list_name = [] 
    num_node = 0
    data = collections.defaultdict(list)
    data['S'] = ['B', 3, 'A', 2, 6]

    data['A'] = ['C', 3, 4]
    data['B'] = ['C', 1, 'D', 3, 4]
    data['C'] = ['D', 1, 'E', 3, 4]
    data['D'] = ['F', 2, 3]
    data['E'] = ['G', 2, 1]
    data['F'] = ['G', 1, 1]
    data['G'] = [0]
    start_node = ''
    goal_node = ''
    result_str = ''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        MainWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Runbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Runbutton.setGeometry(QtCore.QRect(320, 780, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Runbutton.setFont(font)
        self.Runbutton.setObjectName("Runbutton")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(60, 80, 500, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_title.setFont(font)
        self.label_title.setScaledContents(True)
        self.label_title.setObjectName("label_title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 230, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 240, 371, 31))
        self.textEdit.setObjectName("textEdit")
        self.OKbutton = QtWidgets.QPushButton(self.centralwidget)
        self.OKbutton.setGeometry(QtCore.QRect(320, 310, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OKbutton.setFont(font)
        self.OKbutton.setObjectName("OKbutton")
        self.label_node = QtWidgets.QLabel(self.centralwidget)
        self.label_node.setGeometry(QtCore.QRect(60, 380, 231, 51))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 450, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_node.setFont(font)
        self.label_node.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 530, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 610, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 670, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 670, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(290, 460, 371, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(290, 540, 371, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(290, 620, 371, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(590, 720, 50, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(700, 720, 50, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_op = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_op.setGeometry(QtCore.QRect(900, 150, 551, 611))
        self.textEdit_op.setObjectName("textEdit_op")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 700, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.textEdit_op.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.OKbutton.clicked.connect(self.OK)
        self.pushButton.clicked.connect(self.Next)
        # self.Runbutton.clicked.connect(self.Run)
        self.Runbutton.clicked.connect(self.A_star)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Giải thuật A*"))
        self.Runbutton.setText(_translate("MainWindow", "RUN"))
        self.label.setText(_translate("MainWindow", "Danh sách các nút"))
        self.OKbutton.setText(_translate("MainWindow", "OK"))
        self.label_title.setText(_translate("MainWindow", "Tool thuật toán A*"))
        self.label_node.setText(_translate("MainWindow", "Thông tin nút"))
        self.label_2.setText(_translate("MainWindow", "Các nút kề "))
        self.label_3.setText(_translate("MainWindow", "Cost tương ứng"))
        self.label_4.setText(_translate("MainWindow", "Hàm Heuristic"))
        self.label_5.setText(_translate("MainWindow", "Start"))
        self.label_6.setText(_translate("MainWindow", "Goal"))
        self.textEdit_op.setText(_translate("MainWindow", "Kết quả duyệt và đường đi"))
        self.pushButton.setText(_translate("MainWindow", "Next"))


    def OK(self):
        _translate = QtCore.QCoreApplication.translate
        string =str(self.textEdit.toPlainText())
        if not string:
            mess = QMessageBox()
            mess.setWindowTitle('Lỗi')
            mess.setText('Chưa nhập danh sách các nút kìa bạn ơi')
            mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
            mess.setStandardButtons(QMessageBox.Ok)
            mess.setDefaultButton(QMessageBox.Ok)
            x = mess.exec_()
        else:

            self.list_name=string.split()
            self.num_node = len(self.list_name)
            # print(string)
            # self.textEdit_op.setText()
            self.textEdit_op.setText(_translate("MainWindow", f"{self.list_name}"))
            self.label_node.setText(_translate("MainWindow", "Thông tin nút {}".format(self.list_name[0])))

    def Next(self):
        _translate = QtCore.QCoreApplication.translate
        if not self.textEdit_2.toPlainText():
            mess = QMessageBox()
            mess.setWindowTitle('Lỗi')
            mess.setText('Chưa nhập các nút kề kìa bạn ơi!')
            mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
            mess.setStandardButtons(QMessageBox.Ok)
            mess.setDefaultButton(QMessageBox.Ok)
           
            x = mess.exec_()
        elif not self.textEdit_3.toPlainText():
            mess = QMessageBox()
            mess.setWindowTitle('Lỗi')
            mess.setText('Chưa nhập đường đi tương ứng kìa bạn ơi')
            mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
            mess.setStandardButtons(QMessageBox.Ok)
            mess.setDefaultButton(QMessageBox.Ok)
           
            x = mess.exec_()
        elif not self.textEdit_4.toPlainText():
            mess = QMessageBox()
            mess.setWindowTitle('Lỗi')
            mess.setText('Chưa nhập Heuristic kìa bạn ơi')
            mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
            mess.setStandardButtons(QMessageBox.Ok)
            mess.setDefaultButton(QMessageBox.Ok)
            
            x = mess.exec_()
        else:
            i =  self.num_node - len(self.list_name)
            # print(i)
            node_nei = [str(node) for node in self.textEdit_2.toPlainText().split()]
            cost_nei = [int(cost) for cost in self.textEdit_3.toPlainText().split()]
            heuristic = int(self.textEdit_4.toPlainText())
            Nei = []
            for j in range(len(node_nei)):
                Nei.append(node_nei[j])
                Nei.append(cost_nei[j])
            Nei.append(heuristic)
            self.data[self.list_name[i]] = Nei
            if i == len(self.list_name)-2:
                self.data[self.list_name[-1]] = [0] 
            self.num_node+=1
            self.label_node.setText(_translate("MainWindow", f"Thông tin nút {self.list_name[i+1]}"))
            self.textEdit_2.setText('')
            self.textEdit_3.setText('')
            self.textEdit_4.setText('')
            self.textEdit_op.setText(_translate("MainWindow", f"{self.data}"))
    def Run(self):
        print(self.result_str)
        _translate = QtCore.QCoreApplication.translate
        # A_star( Node('S'),  Node('G'), self.data)
        self.textEdit_op.setText(_translate("MainWindow", f"{self.result_str}"))
    def A_star(self):
        _translate = QtCore.QCoreApplication.translate
        road = []
        self.start_node = str(self.textEdit_5.toPlainText())
        self.goal_node = str(self.textEdit_6.toPlainText())
        S = Node(name = self.start_node)
        G = Node(name = self.goal_node)
        Open = queue.PriorityQueue()
        Close = queue.PriorityQueue()
        S.h = self.data[S.name][-1] #Lấy chỉ số heuristic
        Open.put(S)             # Đẩy S vào hàng đợi
        while True:
            if Open.empty():    #Hàng đợi trống và kết thúc với ko có đường đi
                print('Tìm kiếm thất bại!')
                break
            O = Open.get()      #Lấy phần tử được ưu tiên nhất
            if CheckInQueue(O, Close):
                continue
            Close.put(O)        
            # print('Duyet {} {} {}'.format(O.name, O.g, O.h))
            self.result_str += 'Duyệt {} {} {} \n'.format(O.name, O.g, O.h)
            if equal(O, G):
                # print('Tìm kiếm thành công')
                self.result_str += 'Tìm kiếm thành công\n'
                get_path(O, road)                     #Suy ra đường đi khi đến đích
                for node in road:
                    if node == S.name:
                        self.result_str += f'{S.name}\n'
                        # print("S")
                    else:
                        self.result_str += "{} <- ".format(node)
                        # print("{} -> ".format(node), end = '')
                # print('Khoảng cách: {}'.format(O.h+O.g))    
                self.result_str+='Khoảng cách: {}'.format(O.h+O.g)
                break
            i= 0
            while i< len(self.data[O.name]) -1:      #Duyệt theo thuật toán ưu tiên f(x) 
                name = self.data[O.name][i]
                g = O.g + self.data[O.name][i+1]
                h = self.data[name][-1]
                tmp =  Node(name = name, g = g, h=h)
                tmp.par = O

                kks1 = False
                kks2 = CheckInQueue(tmp, Close)
                if not kks1 and not kks2:
                    Open.put(tmp)
                i+=2
        print(self.result_str)
        # A_star( Node('S'),  Node('G'), self.data)
        self.textEdit_op.setText(_translate("MainWindow", f"{self.result_str}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

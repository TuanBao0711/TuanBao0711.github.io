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

# def check_ip(a, b):
# 	return (set(a).issubset(set(b)))
	
# def check_ip_number(lst):
# 	for i in lst:
# 		if

class Ui_MainWindow_UCS(object):
	list_name = [] 
	num_node = 0
	data = collections.defaultdict(list)
	# data['S'] = ['A', 3, 'B', 5]
	# data['A'] = ['C', 4, 'D', 1]
	# data['B'] = ['D',4]
	# data['C'] = ['E',1]
	# data['D'] = ['E',1,'F', 2]
	# data['E'] = ['G',6]
	# data['F'] = ['E',1]
	
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
	    font = QtGui.QFont()
	    font.setPointSize(12)
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
	    self.textEdit_op = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_op.setGeometry(QtCore.QRect(900, 150, 551, 611))
	    self.textEdit_op.setObjectName("textEdit_op")
	    self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_5.setGeometry(QtCore.QRect(590, 720, 50, 31))
	    self.textEdit_5.setObjectName("textEdit_5")
	    self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_6.setGeometry(QtCore.QRect(700, 720, 50, 31))
	    self.textEdit_6.setObjectName("textEdit_6")
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
	    # # self.Runbutton.clicked.connect(self.Run)
	    self.Runbutton.clicked.connect(self.UCS)
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "UCS"))
		self.Runbutton.setText(_translate("MainWindow", "RUN"))
		self.label.setText(_translate("MainWindow", "Danh sách các nút"))
		self.OKbutton.setText(_translate("MainWindow", "OK"))
		self.label_title.setText(_translate("MainWindow", "Tool thuật toán UCS"))
		self.label_node.setText(_translate("MainWindow", "Thông tin nút"))
		self.label_2.setText(_translate("MainWindow", "Các nút kề "))
		self.label_3.setText(_translate("MainWindow", "Cost tương ứng"))
		self.label_5.setText(_translate("MainWindow", "Start"))
		self.label_6.setText(_translate("MainWindow", "Goal"))
		self.textEdit_op.setText(_translate("MainWindow", "Kết quả duyệt và đường đi"))
		self.pushButton.setText(_translate("MainWindow", "Next"))
	def OK(self):
		_translate = QtCore.QCoreApplication.translate
		string =str(self.textEdit.toPlainText())
		lst_ip = string.split()
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
		string =str(self.textEdit.toPlainText())
		lst_ip = string.split()
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

		# 	x = mess.exec_()
		# elif kks not in self.list_name  :
		# 	mess = QMessageBox()
		# 	mess.setWindowTitle('Lỗi')
		# 	mess.setText('Nhập nhầm nút ngoài danh sách ban đầu')
		# 	mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
		# 	mess.setStandardButtons(QMessageBox.Ok)
		# 	mess.setDefaultButton(QMessageBox.Ok)
		# 	x = mess.exec_()

		else:
			i =  self.num_node - len(self.list_name)
			# print(i)
			node_nei = [str(node) for node in self.textEdit_2.toPlainText().split()]
			cost_nei = [int(cost) for cost in self.textEdit_3.toPlainText().split()]
			Nei = []
			for j in range(len(node_nei)):
			    Nei.append(node_nei[j])
			    Nei.append(cost_nei[j])
			self.data[self.list_name[i]] = Nei
			if i == len(self.list_name)-2:
			    self.data[self.list_name[-1]] = [0] 
			self.num_node+=1
			self.label_node.setText(_translate("MainWindow", f"Thông tin nút {self.list_name[i+1]}"))
			self.textEdit_2.setText('')
			self.textEdit_3.setText('')
			self.textEdit_op.setText(_translate("MainWindow", f"{self.data}"))


	def UCS(self):
		_translate = QtCore.QCoreApplication.translate
		self.start_node = str(self.textEdit_5.toPlainText())
		self.goal_node = str(self.textEdit_6.toPlainText())
		S = Node(name = self.start_node)
		G = Node(name = self.goal_node)
		road = []
		Open = queue.PriorityQueue()
		Close = queue.PriorityQueue()
		Open.put(S)
		while True:
		    if Open.empty():    
		        self.result_str += 'Tìm kiếm thất bại!'
		        break
		    O = Open.get()
		    if CheckInQueue(O, Close):
		        continue     
		    Close.put(O)        
		    # print('Duyet {} {}'.format(O.name, O.g))
		    self.result_str += 'Duyệt {} {} \n'.format(O.name, O.g)
		    if equal(O, G):
		        # print('Tìm kiếm thành công')
		        self.result_str += 'Tìm kiếm thành công\n'
		        get_path(O, road)                     
		        # print('Khoảng cách: {}'.format(O.h+O.g))    
		        for node in road:
		            if node == S.name:
		                self.result_str += f'{S.name}\n'
		                # print("S")
		            else:
		                self.result_str += "{} <- ".format(node)
		        self.result_str += 'Khoảng cách: {}\n'.format(O.g)
		        break
		    i = 0
		    while i< len(self.data[O.name]) -1:      #Duyệt theo thuật toán ưu tiên f(x) 
		        name = self.data[O.name][i]
		        g = O.g + self.data[O.name][i+1]
		        tmp =  Node(name = name, g = g)
		        tmp.par = O
		        kks1 = False
		        kks2 = CheckInQueue(tmp, Close)
		        if not kks1 and not kks2:
		            Open.put(tmp)
		        i+=2
		print(self.result_str)
		self.textEdit_op.setText(_translate("MainWindow", f"{self.result_str}"))
		self.data.clear()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import collections
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


#----------------------------


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


class Ui_MainWindow_BFS(object):
	list_name = [] 
	num_node = 0
	data = collections.defaultdict(list)
	# data['S'] = ['A',  'B']
	# data['A'] = ['C',  'D']
	# data['B'] = ['D']
	# data['C'] = ['E']
	# data['D'] = ['E','F']
	# data['E'] = ['G']
	# data['F'] = ['E']
	result_str = ''
	start_node = ''
	goal_node = ''
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
	    self.label_node.setGeometry(QtCore.QRect(60, 400, 231, 51))
	    self.label_2 = QtWidgets.QLabel(self.centralwidget)
	    self.label_2.setGeometry(QtCore.QRect(60, 480, 231, 51))
	    font = QtGui.QFont()
	    font.setPointSize(12)
	    self.label_node.setFont(font)
	    self.label_node.setObjectName("label_2")
	    self.label_2.setFont(font)
	    self.label_2.setObjectName("label_2")
	    self.label_3 = QtWidgets.QLabel(self.centralwidget)
	    self.label_3.setGeometry(QtCore.QRect(190, 670, 231, 51))
	    font = QtGui.QFont()
	    font.setPointSize(12)
	    self.label_3.setFont(font)
	    self.label_3.setObjectName("label_3")
	    self.label_4 = QtWidgets.QLabel(self.centralwidget)
	    self.label_4.setGeometry(QtCore.QRect(450, 670, 231, 51))
	    font = QtGui.QFont()
	    font.setPointSize(12)
	    self.label_4.setFont(font)
	    self.label_4.setObjectName("label_3")
	    font = QtGui.QFont()
	    font.setPointSize(12)
	    self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_2.setGeometry(QtCore.QRect(290, 490, 371, 31))
	    self.textEdit_2.setObjectName("textEdit_2")
	    self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_3.setGeometry(QtCore.QRect(290, 680, 50, 31))
	    self.textEdit_3.setObjectName("textEdit_3")
	    self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_4.setGeometry(QtCore.QRect(540, 680, 50, 31))
	    self.textEdit_4.setObjectName("textEdit_3")
	    self.textEdit_op = QtWidgets.QTextEdit(self.centralwidget)
	    self.textEdit_op.setGeometry(QtCore.QRect(900, 150, 551, 611))
	    self.textEdit_op.setObjectName("textEdit_op")
	    self.pushButton = QtWidgets.QPushButton(self.centralwidget)
	    self.pushButton.setGeometry(QtCore.QRect(320, 580, 181, 51))
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
	    self.Runbutton.clicked.connect(self.DFS)
	def retranslateUi(self, MainWindow):
	    _translate = QtCore.QCoreApplication.translate
	    MainWindow.setWindowTitle(_translate("MainWindow", "Giải thuật BFS"))
	    self.Runbutton.setText(_translate("MainWindow", "RUN"))
	    self.label.setText(_translate("MainWindow", "Danh sách các nút"))
	    self.OKbutton.setText(_translate("MainWindow", "OK"))
	    self.label_title.setText(_translate("MainWindow", "Tool thuật toán BFS"))
	    self.label_node.setText(_translate("MainWindow", "Thông tin nút"))
	    self.label_2.setText(_translate("MainWindow", "Các nút kề "))
	    self.label_3.setText(_translate("MainWindow", "Start"))
	    self.label_4.setText(_translate("MainWindow", "Goal"))
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
		# string =str(self.textEdit.toPlainText())
		# lst_ip = string.split()
		# if not self.textEdit_2.toPlainText():
		# 	mess = QMessageBox()
		# 	mess.setWindowTitle('Lỗi')
		# 	mess.setText('Chưa nhập các nút kề kìa bạn ơi!')
		# 	mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
		# 	mess.setStandardButtons(QMessageBox.Ok)
		# 	mess.setDefaultButton(QMessageBox.Ok)
		# 	x = mess.exec_()

		# 	x = mess.exec_()
		# elif kks not in self.list_name  :
		# 	mess = QMessageBox()
		# 	mess.setWindowTitle('Lỗi')
		# 	mess.setText('Nhập nhầm nút ngoài danh sách ban đầu')
		# 	mess.setIcon(QMessageBox.Warning)  #Critical, Warning, Information, Question
		# 	mess.setStandardButtons(QMessageBox.Ok)
		# 	mess.setDefaultButton(QMessageBox.Ok)
		# 	x = mess.exec_()

		# else:
		i =  self.num_node - len(self.list_name)
		# print(i)
		node_nei = [str(node) for node in self.textEdit_2.toPlainText().split()]
		Nei = []
		for j in range(len(node_nei)):
		    Nei.append(node_nei[j])
		self.data[self.list_name[i]] = Nei
		if i == len(self.list_name)-2:
		    self.data[self.list_name[-1]] = [] 
		self.num_node+=1
		self.label_node.setText(_translate("MainWindow", f"Thông tin nút {self.list_name[i+1]}"))
		self.textEdit_2.setText('')
		self.textEdit_op.setText(_translate("MainWindow", f"{self.data}"))

	def DFS(self):
		_translate = QtCore.QCoreApplication.translate
		self.start_node = str(self.textEdit_3.toPlainText())
		self.goal_node = str(self.textEdit_4.toPlainText())
		S = Node(name = self.start_node)
		G = Node(name = self.goal_node)
		road = []
		# S =  Node(name = start)
		#    G =  Node(name = goal)
		Open = []
		Close = []
		Open.append(S)
		while True:
			if len(Open) == 0:
				self.result_str = 'Tìm kiếm thất bại'
				break
			O = Open.pop(0)
			Close.append(O)
			self.result_str += f'Duyệt {O.name}\n'
			if equal(O, G):
				self.result_str += 'Tìm kiếm thành công\n'
				path(O, road)
				for node in road:
					if node == self.start_node:
					    self.result_str += f'{self.start_node}\n'
					    # print("S")
					else:
					    self.result_str += "{} <- ".format(node)
				break
			for x in self.data[O.name]:
				tmp = Node(x)
				tmp.par = O
				check1 = check(tmp, Open)
				check2 = check(tmp, Close)
				if not check1 and not check2:
					Open.append(tmp)

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

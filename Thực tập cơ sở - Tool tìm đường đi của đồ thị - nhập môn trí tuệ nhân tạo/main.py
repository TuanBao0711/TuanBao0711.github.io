import sys 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from demo_DFS import Ui_MainWindow_DFS
from demo_BFS import Ui_MainWindow_BFS
from demo_a_star import Ui_MainWindow_A
from demo_UCS import Ui_MainWindow_UCS
from home import Ui_MainWindow

class MainWindow:
	def __init__ (self):
		self.main_win = QMainWindow()
		self.uic = Ui_MainWindow()
		self.uic.setupUi(self.main_win)
		self.uic.BFSButton.clicked.connect(self.Run_BFS)
		self.uic.DFSButton.clicked.connect(self.Run_DFS)
		self.uic.UCSButton.clicked.connect(self.Run_UCS)
		self.uic.ASButton.clicked.connect(self.Run_AS)
	def show(self):
		self.main_win.show()


	def Run_BFS(self):
		self.BFS_window = QMainWindow()
		self.uicBFS = Ui_MainWindow_BFS()
		self.uicBFS.setupUi(self.BFS_window)
		self.BFS_window.show()
	def Run_DFS(self):
		self.DFS_window = QMainWindow()
		self.uicDFS = Ui_MainWindow_DFS()
		self.uicDFS.setupUi(self.DFS_window)
		self.DFS_window.show()
	def Run_UCS(self):
		self.UCS_window = QMainWindow()
		self.uicUCS = Ui_MainWindow_UCS()
		self.uicUCS.setupUi(self.UCS_window)
		self.UCS_window.show()
	def Run_AS(self):
		self.AS_window = QMainWindow()
		self.uicAS = Ui_MainWindow_A()
		self.uicAS.setupUi(self.AS_window)
		self.AS_window.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec())
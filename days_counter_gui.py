from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from days_counter import *
import sys


class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__() #calling parent constructor
		self.setGeometry(50, 50, 600, 300) #(xpos, ypos, width, height)
		self.setWindowTitle("Days Counter")
		self.initUI()
		self.setDefault()
		self.daysOfMonths=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	def initUI(self): #all the widgets that goes in the window are initialize here
		self.welcomeLabel = QtWidgets.QLabel(self)
		self.welcomeLabel.setText("Welcome to this simple days counter program!")
		self.welcomeLabel.move(10,10)

		self.enterd1 = QLineEdit(self) 
		self.enterd1.move(30,90)
		self.enterm1 = QLineEdit(self) 
		self.enterm1.move(210,90)
		self.entery1 = QLineEdit(self) 
		self.entery1.move(390,90)
		self.enterd2 = QLineEdit(self) 
		self.enterd2.move(30,150)
		self.enterm2 = QLineEdit(self) 
		self.enterm2.move(210,150)
		self.entery2 = QLineEdit(self) 
		self.entery2.move(390,150)

		self.button=QPushButton("Count days!", self) #button for setting the parameter values
		self.button.move(220,200)
		self.button.clicked.connect(self.save_param)
		self.update()

	def setDefault(self):
		self.enterd1.setPlaceholderText("start day")
		self.enterm1.setPlaceholderText("start month")
		self.entery1.setPlaceholderText("start year")
		self.enterd2.setPlaceholderText("end day")
		self.enterm2.setPlaceholderText("end month")
		self.entery2.setPlaceholderText("end year")
	
	def update(self):
		self.welcomeLabel.adjustSize()
		self.enterd1.adjustSize()
		self.enterm1.adjustSize()
		self.entery1.adjustSize()
		self.enterd2.adjustSize()
		self.enterm2.adjustSize()
		self.entery2.adjustSize()
	
	def save_param(self):
		try:
			self.d1= int(self.enterd1.text())
			self.m1= int(self.enterm1.text())
			self.y1= int(self.entery1.text())
			self.d2= int(self.enterd2.text())
			self.m2= int(self.enterm2.text())
			self.y2= int(self.entery2.text())
			if self.d1 <= 0 or self.m1 <= 0 or self.y1 <= 0 or self.d2 <= 0 or self.m2 <= 0 or self.y2 <= 0:
				raise ValueError
			if self.d1 == None or self.m1 == None or self.y1 == None or self.d2 == None or self.m2 == None or self.y2 == None:
				raise emptyBoxError 
			if self.m1>12 or self.m2>12:
				raise monthRangeError
			if self.d1>31 or self.d2>31:
				raise dayRangeError
			if self.d1>self.daysOfMonths[self.m1-1]:
				if self.m1!=2: 
					raise dateDoesNotExistError
				elif daysCounter.isLeapYear(self.y1) is False:
					raise dateDoesNotExistError 
					
			if self.d2>self.daysOfMonths[self.m2-1]:
				if self.m2!=2: 
					raise dateDoesNotExistError
				elif daysCounter.isLeapYear(self.y2) is False:
					raise dateDoesNotExistError
			if self.y2<self.y1:
				raise dateRangeError
			elif self.y1==self.y2 and self.m2<self.m1:
				raise dateRangeError
			elif self.y1==self.y2 and self.m2==self.m1 and self.d2<self.d1:
				raise dateRangeError
			
			days=daysCounter(self.y1,self.m1, self.d1, self.y2, self.m2,  self.d2)
			print(days.countDays())
		except emptyBoxError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("All entries need to be filled!")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()

		except ValueError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("The inputs must only be positive numbers! Try again")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()

		except monthRangeError:
			msg = QMessageBox()
			msg.setWindowTitle("Month Range Error")
			msg.setText("Month must be between 1 and 12")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()
		except dayRangeError:
			msg = QMessageBox()
			msg.setWindowTitle("Days Range Error")
			msg.setText("Day must be between 1 and 31")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()
		except dateDoesNotExistError:
			msg = QMessageBox()
			msg.setWindowTitle("Invalid date")
			msg.setText("Please enter a valid date")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()
		except dateRangeError:
			msg = QMessageBox()
			msg.setWindowTitle("Invalid date Range")
			msg.setText("End date must be greater than start date")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()

class monthRangeError(Exception):
	pass
class dayRangeError(Exception):
	pass
class emptyBoxError(Exception):
	pass
class dateDoesNotExistError(Exception):
	pass
class dateRangeError(Exception):
	pass




if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_()) 



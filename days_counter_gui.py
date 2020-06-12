from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from days_counter import *
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__() #calling parent constructor
		self.setGeometry(50, 50, 620, 300) #(xpos, ypos, width, height)
		self.setWindowTitle("Days Counter")
		self.initUI()
		self.setDefault()
		self.daysOfMonths=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	def initUI(self): #all the widgets that goes in the window are initialize here
		self.welcomeLabel = QtWidgets.QLabel(self)
		self.welcomeLabel.setText("Welcome to this simple days counter program!")
		self.welcomeLabel.move(20, 20)
		#show the user an example of an input value
		self.instructionLabel = QtWidgets.QLabel(self)
		self.instructionLabel.setText("For example, to enter 1st December 2020, enter '1', '12', '2020' in the entry fields")
		self.instructionLabel.move(20, 60)
		#entry fields
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
		#button for setting the parameter values
		self.button=QPushButton("Count days!", self) 
		self.button.move(230,200)
		self.button.clicked.connect(self.save_param)
		#label that gets updated to show the result (num of days)
		self.dayLabel = QtWidgets.QLabel(self)
		self.dayLabel.setText("")
		self.dayLabel.move(10,250)
		#label that gets updated to show the result (num of months)
		self.monthLabel = QtWidgets.QLabel(self)
		self.monthLabel.setText("")
		self.monthLabel.move(10,280)
		#size update
		self.update()

	def setDefault(self):
		#entry fields with placeholders
		self.enterd1.setPlaceholderText("start day")
		self.enterm1.setPlaceholderText("start month")
		self.entery1.setPlaceholderText("start year")
		self.enterd2.setPlaceholderText("end day")
		self.enterm2.setPlaceholderText("end month")
		self.entery2.setPlaceholderText("end year")
	
	def update(self):
		#adjust label sizing
		self.welcomeLabel.adjustSize()
		self.enterd1.adjustSize()
		self.enterm1.adjustSize()
		self.entery1.adjustSize()
		self.enterd2.adjustSize()
		self.enterm2.adjustSize()
		self.entery2.adjustSize()
		self.dayLabel.adjustSize()
		self.instructionLabel.adjustSize()
	
	def save_param(self):
		#handling invalid user inputs
		try:
			self.d1= int(self.enterd1.text())
			self.m1= int(self.enterm1.text())
			self.y1= int(self.entery1.text())
			self.d2= int(self.enterd2.text())
			self.m2= int(self.enterm2.text())
			self.y2= int(self.entery2.text())
			#ensures entered values are all positive integers
			if self.d1 <= 0 or self.m1 <= 0 or self.y1 <= 0 or self.d2 <= 0 or self.m2 <= 0 or self.y2 <= 0:
				raise ValueError
			#checks if all entry boxes are filled
			if self.d1 == None or self.m1 == None or self.y1 == None or self.d2 == None or self.m2 == None or self.y2 == None:
				raise emptyBoxError 
			#checks if month value lies withing 1-12
			if self.m1>12 or self.m2>12:
				raise monthRangeError
			#checks if month value lies within 1-30/31
			if self.d1>31 or self.d2>31:
				raise dayRangeError
			#allows day 29 for the month of february only if it is a leap year
			if self.d1>self.daysOfMonths[self.m1-1]:
				if self.m1==2 and daysCounter.isLeapYear(self.y1) is True and self.d1==29:
					pass
				else: 
					raise dateDoesNotExistError
			if self.d2>self.daysOfMonths[self.m2-1]:
				if self.m2==2 and daysCounter.isLeapYear(self.y2) is True and self.d2==29:
					pass
				else: 
					raise dateDoesNotExistError
			#ensures that start date is smaller than end date
			if self.y2<self.y1:
				raise dateRangeError
			elif self.y1==self.y2 and self.m2<self.m1:
				raise dateRangeError
			elif self.y1==self.y2 and self.m2==self.m1 and self.d2<self.d1:
				raise dateRangeError
			#creates an daysCounter object
			days=daysCounter(self.y1,self.m1, self.d1, self.y2, self.m2,  self.d2)
			self.dayLabel.setText("The total number of days is: {}".format(days.countDays()))
			#self.monthLabel.setText("The total number of complete months is: {}".format(int(days.countDays()/30)))
			self.dayLabel.adjustSize()
			self.monthLabel.adjustSize()
			
		except emptyBoxError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("All entries need to be filled!")
			msg.setIcon(QMessageBox.Information)
			msg.exec_()
		except ValueError:
			msg = QMessageBox()
			msg.setWindowTitle("Input Error")
			msg.setText("The inputs must only be positive integers! Try again")
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



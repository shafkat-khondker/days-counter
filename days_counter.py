"""
Given your birthday and the current date, calculate number of days between two 
Compensate for leap days
If you were born 1 Jan 2012, and today's date is Jan 2012, you are 1 day old
"""

class daysCounter():
	def __init__(self, y1, m1, d1, y2, m2, d2):
		self.y1=y1
		self.m1=m1
		self.d1=d1
		self.y2=y2
		self.m2=m2
		self.d2=d2
		self.daysOfMonths=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		self.daysOfYear=365

	@classmethod
	def isLeapYear(cls, year):
		if year%4 != 0:
			return False
		elif year%100 !=0:
			return True 
		elif year%400 !=0:
			return False
		else:
			return True

	def countDays(self):
		days=0
		currentYear=self.y1
		currentMonth=self.m1
		if self.y1 == self.y2:
			return self.sameYear(self.y1, self.m1, self.d1, self.m2, self.d2)
		else:
			days+=self.sameYear(self.y1,self.m1,self.d1,12,31)
			while self.y2-currentYear>1:
				if self.isLeapYear(currentYear+1) is True:
					days+=(self.daysOfYear+1)
				else:
					days+=self.daysOfYear
				currentYear+=1
			days+=self.sameYear(self.y2, 1, 1, self.m2, self.d2)
			return days+1 

	def sameYear(self, y1, m1, d1, m2, d2):
		days=0
		currentMonth=m1
		if currentMonth == m2:
			return d2-d1
		else:
			days+=self.daysOfMonths[currentMonth-1]-d1
			while m2-currentMonth>1:
				if currentMonth==1 and self.isLeapYear(y1) is True:
					days+=29
				else:
					days+=self.daysOfMonths[currentMonth]
				currentMonth+=1	
			days+=d2
			return days


#d=daysCounter(1997,11,5,2020,6,11)
#print(d.countDays())

__author__="felsamps"
__date__ ="$04/08/2010 20:04:15$"

from collections import *

class MbAccess:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.list = deque()
		self.acc = 0

	def insertRefBlock(self, x, y, w, h):
		if [x,y,w,h] not in self.list:
			self.list.append([x,y,w,h])
			self.acc += w*h			

	def popRefBlock(self):
		return self.list.popleft()

	def empty(self):
		if len(self.list) == 0:
			return True
		return False

	def size(self):
		return len(self.list)

	def getAcc(self):
		return self.acc
	
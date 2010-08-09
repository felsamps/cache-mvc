__author__="felsamps"
__date__ ="$02/08/2010 10:59:13$"

class LogFile():
	def __init__(self):
		self.setEnableLog(True)

	def log(self, str):
		if self.enabled == True:
			print str

	def setEnableLog(self, bool):
		self.enabled = bool

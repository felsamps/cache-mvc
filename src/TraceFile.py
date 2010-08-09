__author__="felsamps"
__date__ ="$04/08/2010 17:33:52$"

from MbAccess import *

class TraceFile:
	def __init__(self, filePath):
		self.file = open(filePath,"rb")
		self.file.seek(0,2)
		self.size = self.file.tell()
		self.file.seek(0,0)

	def _readInt(self):
		str = self.file.readline()
		str = str[:-1]
		return int(str)

	def _finished(self):
		if self.size <= self.file.tell():
			return True
		return False

	def readMb(self):
		mbAccess = MbAccess(self._readInt(), self._readInt())
		for i in range(0, self._readInt()):
			mbAccess.insertRefBlock(self._readInt(),
									self._readInt(),
									self._readInt(),
									self._readInt())
		return mbAccess
	
	

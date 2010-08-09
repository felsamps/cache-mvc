__author__="felsamps"
__date__ ="$04/08/2010 21:02:50$"

from Cache import *
from ConfigFile import *
from MMU import *
from MbAccess import *
from Stats import *

from Stats import *
from collections import *

import sys

RASTER = 0
ZZ = 1
HF3V2 = 2

class SearchEngine:
	def __init__(self, traceFile, configFile):
		"""Search Engine Constructor"""
		self.stats = Stats()
		self.width = configFile.getFrameW()
		self.height = configFile.getFrameH()
		self.mmu = MMU(configFile, self.stats)
		self._initMbArrayOrder(configFile)
		self._initMbMatrix(traceFile)
		self.logger = LogFile()
		self.logger.setEnableLog(False)

	def _initMbMatrix(self, traceFile):
		self.matrix = []
		for x in range(0,self.width/16):
			row = []
			for y in range(0,self.height/16):
				mb = traceFile.readMb()
				row.append(mb)
				self.stats.addSamples(mb.getAcc())
			self.matrix.append(row)
			
	
	def _initMbArrayOrder(self, configFile):
		# @type configFile ConfigFile
		self.mbOrder = deque()
		if configFile.getMbOrder() == RASTER:
			self._rasterOrder()
		elif configFile.getMbOrder() == ZZ:
			self._ZZOrder()
		elif configFile.getMbOrder() == HF3V2:
			self._HF3V2Order()
		
	def _rasterOrder(self):
		for j in range(0, self.height/16):
			for i in range(0, self.width/16):
				self.mbOrder.append([i,j])

	def _ZZOrder(self):
		order = []
		order.append([0,0])
		order.append([0,1])
		order.append([1,0])
		order.append([1,1])
		for j in range(0, self.height/16, 2):
			for i in range(0, self.height/16, 2):
				for k in range(0, 4):
					self.mbOrder.append([j+order[k][0], i+order[k][1]])

	def _HF3V2Order(self): #REFS CHEN, 2006: IEEE TCSVT
		m = 3
		n = 2
		for i in range(0, self.height/16, n):
			hor = [0 for it in range(0,n)]
			[self.mbOrder.append([var,i]) for var in range(0,m-1)]
			hor[0] = hor[0] + n
			while hor[0] < self.width/16:
				for k in range(0,n):
					self.mbOrder.append([hor[k],i+k])
					hor[k] = hor[k] + 1
			[self.mbOrder.append([hor[n-1]+var,i+(n-1)]) for var in range(0,m-1)]
					
	def process(self):
		# @type mb MbAccess
		for l in self.mbOrder:
			mb = self.matrix[l[0]][l[1]]
			self.logger.log("Performing access to the current MB: " + str(l[0]) + " " + str(l[1]) + " " + str(mb.size()))
			while mb.empty() != True:
				access = mb.popRefBlock()
				if self._isValidAccess(access):
					self.mmu.performAccessBlock(access)
				else:
					self.stats.addOutOfFramesBlock(1)
			#self.mmu.printCache()
			#a = sys.stdin.read(1)
		#self.mmu.report()

	def _isValidAccess(self, access):
		if access[0] < 0 or access[1] < 0 or (access[0]+access[2]) > self.width or (access[1]+access[3] > self.height):
			return False
		return True

	def getStats(self):
		return self.stats
		
__author__="felsamps"
__date__ ="$03/08/2010 10:06:27$"

from LogFile import *
from Cache import *

class MMU:
	def __init__(self, config):
		self._initCacheAtts(config)
		self._initCacheMapping()
		self._initCache()
		self._logCacheConfigs()

	def _logCacheConfigs(self):
		self.logger.log("To be implemented")

	def _initCacheAtts(self, config):
		self.frameW = config.getFrameW()
		self.frameH = config.getFrameH()
		self.blockW = config.getBlockW()
		self.blockH = config.getBlockH()
		self.setSize = config.getSetSize()
		self.numBlocks = config.getNumBlocks()
		self.rows = config.getRows()
		self.columns = config.getColumns()
		self.blocksW = self.frameW / self.blockW
		self.blocksH = self.frameH / self.blockH
		self._initBasicMapping()
		self.logger = LogFile("cache.log")

	def _initBasicMapping(self):
		self.basicMapping = []
		cont = 0
		for y in range(0,self.rows):
			row = []
			for x in range(0,self.columns):
				row.append(cont)
				cont = cont + 1
			self.basicMapping.append(row)
			print row

	def _getCachePosition(self,x,y):
		normX = x % self.columns
		normY = y % self.rows
		return self.basicMapping[normY][normX]

	def _initCacheMapping(self):
		self.mapping = []
		for y in range(0,self.blocksH):
			for x in range(0,self.blocksW):
				self.mapping.append(self._getCachePosition(x,y))
		print self.mapping


	def _initCache(self):
		self.cache = Cache(self.numBlocks, self.setSize, self.rows, self.columns, self.blockW, self.blockH)
		
	def performAccess(self, x, y):
		frameBlock = self._calculateFrameBlock(x, y)
		cachePosition = self.mapping[frameBlock]
		self.cache.accessBlock(cachePosition, frameBlock)

	def _calculateFrameBlock(self, x, y):
		blockX = (x / self.blockW)
		blockY = (y / self.blockH)
		pos = blockY * self.blocksW + blockX
		return pos

	def printStats(self):
		self.cache.printStats()
	
from LogFile import *

__author__="felsamps"
__date__ ="$16/07/2010 15:30:06$"

class Cache:
	def __init__(self, config):
		self._initCacheAtts(config)
		self._initCacheMapping()
		self._initCache()
		self._logCacheConfigs()

	def _logCacheConfigs(self):
		self.logger.log("Tests")

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
		print normX, normY
		return self.basicMapping[normY][normX]

	def _initCacheMapping(self):
		self.mapping = []
		for y in range(0,self.blocksH):
			for x in range(0,self.blocksW):
				self.mapping.append(self._getCachePosition(x,y))
		print self.mapping

	def _initCache(self):
		self.cache = []
		for i in range(0,self.numBlocks):
			self.cache.append([])
		print self.cache

	
__author__="felsamps"
__date__ ="$03/08/2010 10:06:27$"

from LogFile import *
from Cache import *

class MMU:
	def __init__(self, config, stats):
		self.stats = stats
		self._initCacheAtts(config)
		self._initCacheMapping()
		self._initCache()
		self._logCacheConfigs()

	def _logCacheConfigs(self):
		self.a = 0

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
		self.logger = LogFile()
		self.stats.initCacheStats(self.blocksW, self.blocksH, config)
		

	def _initBasicMapping(self):
		self.basicMapping = []
		cont = 0
		for y in range(0,self.rows):
			row = []
			for x in range(0,self.columns):
				row.append(cont)
				cont = cont + 1
			self.basicMapping.append(row)

	def _getCachePosition(self,x,y):
		normX = x % self.columns
		normY = y % self.rows
		return self.basicMapping[normY][normX]

	def _initCacheMapping(self):
		self.mapping = []
		for y in range(0,self.blocksH):
			for x in range(0,self.blocksW):
				self.mapping.append(self._getCachePosition(x,y))

	def _initCache(self):
		self.cache = Cache(self.numBlocks, self.setSize, self.rows, self.columns, self.blockW, self.blockH, self.stats)
		
	def performAccess(self, x, y):
		frameBlock = self._calculateFrameBlock(x, y)
		cachePosition = self.mapping[frameBlock]
		#STATS
		if(self.cache.accessBlock(cachePosition, frameBlock)):
			self.stats.incHit()
			self.stats.incHitPerBlock(block)
		else:
			self.stats.incMiss()
			self.stats.incMissPerBlock(block)
		self.stats.addBlockAccess(1)
		self.stats.addLineAccess(16)

	def performAccessBlock(self, access):
		x = access[0]
		y = access[1]
		w = access[2]
		h = access[3]
		for line in range(y, y+h):
			block = []
			block.append(self._calculateFrameBlock(x, line))
			block.append(self._calculateFrameBlock(x+(w-1), line))
			blockSet = set(block)
			for frameBlock in blockSet:
				cachePosition = 0
				if(frameBlock < len(self.mapping)):
					cachePosition = self.mapping[frameBlock]
					#STATS
					if self.cache.accessBlock(cachePosition, frameBlock):
						self.stats.incHit(frameBlock)
					else:
						self.stats.incMiss(frameBlock)
					self.stats.addLineAccess(1)
		self.stats.addBlockAccess(1)


	def _calculateFrameBlock(self, x, y):
		blockX = (x / self.blockW)
		blockY = (y / self.blockH)
		pos = blockY * self.blocksW + blockX
		return pos

	def report(self):
		self.stats.report()

	def printCache(self):
		self.cache.printCache(self.blocksW, self.blocksH)
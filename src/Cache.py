__author__="felsamps"
__date__ ="$16/07/2010 15:30:06$"

from Statistics import *
from collections import *
class Cache:
	def __init__(self, numBlocks, setSize, rows, columns, blockW, blockH):
		self.numBlocks = numBlocks
		self.setSize = setSize
		self.rows = rows
		self.columns = columns
		self.blockW = blockW
		self.blockH = blockH
		self._initCache()
		self.stats = Statistics()

	def _initCache(self):
		self.cache = []
		for i in range(0,self.numBlocks):
			self.cache.append(deque())
		print self.cache

	def accessBlock(self, position, block):
		cacheEntry = self.cache[position]
		if block in cacheEntry: #HIT
			self.stats.addHit()
			return True
		else: #MISS
			if len(cacheEntry) == self.setSize:
				cacheEntry.popleft()
			cacheEntry.append(block)
			self.stats.addMiss()
			return False

	def printStats(self):
		self.stats.printStats()

	


__author__="felsamps"
__date__ ="$16/07/2010 15:30:06$"

from Stats import *
from collections import *

class Cache:
	def __init__(self, numBlocks, setSize, rows, columns, blockW, blockH, stats):
		self.numBlocks = numBlocks
		self.setSize = setSize
		self.rows = rows
		self.columns = columns
		self.blockW = blockW
		self.blockH = blockH
		self._initCache()
		self.stats = stats

	def _initCache(self):
		self.cache = []
		for i in range(0,self.numBlocks):
			self.cache.append(deque())

	def accessBlock(self, position, block):
		cacheEntry = self.cache[position]
		if block in cacheEntry: #HIT
			return True
		else: #MISS
			if len(cacheEntry) == self.setSize:
				cacheEntry.popleft()
			cacheEntry.append(block)
			return False

	def printCache(self, blocksW, blocksH):
		matrix = []
		[matrix.append([]) for i in range(0,blocksH)]
		for line in matrix:
			[line.append(".") for j in range(0,blocksW)]
		for pos in self.cache:
			for block in pos:
				x = block % blocksW
				y = block / blocksW
				matrix[y][x] = block

		for line in matrix:
			print line
				
		


	


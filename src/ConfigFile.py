__author__="felsamps"
__date__ ="$16/07/2010 15:34:56$"

class ConfigFile:
	def __init__(self, fileName):
		self.fileName = fileName
		print "Config file opened..."

	def initConfigs(self, frameW, frameH, blockW, blockH, setSize, numBlocks, rows, columns, order, bma):
		self.frameW = frameW
		self.frameH = frameH
		self.blockW = blockW
		self.blockH = blockH
		self.setSize = setSize
		self.numBlocks = numBlocks
		self.rows = rows
		self.columns = columns
		self.order = order
		self.bma = bma
	
	def parseFile(self):
		"""Parser the config file"""
		self.fp = open(self.fileName)
		readBuff = self.fp.readlines()
		for line in readBuff:
			splitted = line.split()
			if line.find("WIDTH") != -1:
				self.frameW = int(splitted[2])
			if line.find("HEIGHT") != -1:
				self.frameH = int(splitted[2])
			if line.find("BLOCK_W") != -1:
				self.blockW = int(splitted[2])
			if line.find("BLOCK_H") != -1:
				self.blockH = int(splitted[2])
			if line.find("SET_SIZE") != -1:
				self.setSize = int(splitted[2])
			if line.find("NUM_BLOCKS") != -1:
				self.numBlocks = int(splitted[2])
			if line.find("ROWS") != -1:
				self.rows= int(splitted[2])
			if line.find("COLUMNS") != -1:
				self.columns = int(splitted[2])
			if line.find("MB_ORDER") != -1:
				self.order = int(splitted[2])

	def getMbOrder(self):
		return self.order
	def getFrameW(self):
		return self.frameW
	def getFrameH(self):
		return self.frameH
	def getBlockW(self):
		return self.blockW
	def getBlockH(self):
		return self.blockH
	def getSetSize(self):
		return self.setSize
	def getNumBlocks(self):
		return self.numBlocks
	def getRows(self):
		return self.rows
	def getColumns(self):
		return self.columns
	def getBma(self):
		return self.bma

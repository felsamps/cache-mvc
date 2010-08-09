__author__="felsamps"
__date__="$03/08/2010 10:28:36$"

class Stats:

	def __init__(self):
		self.miss = 0
		self.hit = 0
		self.blocks = 0
		self.lines = 0
		self.outOfFrame = 0
		self.samples = 0

	def initCacheStats(self, blocksW, blocksH, config):
		self.cache = [0 for i in range(0, config.getNumBlocks())]
		self.missPerBlock = [0 for i in range(0, blocksH * blocksW)]
		self.hitPerBlock = [0 for i in range(0, blocksH * blocksW)]
		self.blockSizeInBits = config.getBlockH() * config.getBlockW() * 8
		self.cacheSizeInBits = self.blockSizeInBits * config.getNumBlocks() * config.getSetSize()
		self.searchRange = (96*2)*(96*2)
		self.samplesSRBased = (self.searchRange) * (config.getFrameW()/16) * (config.getFrameH()/16)
		self.config = config

	def incMiss(self, block):
		self.miss += 1
		self.missPerBlock[block] += 1

	def incHit(self, block):
		self.hit += 1
		self.hitPerBlock[block] += 1

	def addBlockAccess(self, v):
		self.blocks += v

	def addLineAccess(self, v):
		self.lines += v

	def addOutOfFramesBlock(self, v):
		self.outOfFrame += v

	def addSamples(self, v):
		self.samples += v

	def _calculateAccessedSamples(self):
		acc = 0
		for x in self.missPerBlock:
			acc += x
		return acc * self.blockSizeInBits

	def report(self):
		total = (self.hit + self.miss)*1.0
		print "TOTAL BLOCKS: ", self.blocks
		print "TOTAL ACCESS: ", self.lines
		print "TOTAL OUT-OF-FRAME ACCESS", self.outOfFrame
		print "HITS:", self.hit, str((self.hit*100)/total)+"%"
		print "MISSES:", self.miss, str((self.miss*100)/total)+"%"
		print "CACHE POSITION SIZE:", str(self.blockSizeInBits)+" bits", str(self.blockSizeInBits/1024.0)+" Kbits"
		print "CACHE SIZE:", str(self.cacheSizeInBits)+" bits",  str(self.cacheSizeInBits/1024.0)+ " Kbits"
		print "REQUIRED SAMPLES:", self.samples
		print "SEARCH RANGE BASED SAMPLES:", self.samplesSRBased
		print "ACCESSED SAMPLES:", self._calculateAccessedSamples()

	def printHeader(self, fp):
		line = "block_size,set,n_blocks,mapping,order,bma,total_access,hits,hits(%),misses,misses(%),block_size(bits),cache_size(bits),accessed_samples"
		fp.write(line + "\n")

	def reportFile(self, fp):
		line = ""
		comma = ","
		total = (self.hit + self.miss)*1.0
		line += str(self.config.getBlockW()) + "x" + str(self.config.getBlockH()) + comma
		line += str(self.config.getSetSize()) + comma
		line += str(self.config.getNumBlocks()) + comma
		line += str(self.config.getRows()) + "x" + str(self.config.getColumns()) + comma
		line += str(self.config.getMbOrder()) + comma
		line += str(self.config.getBma()) + comma
		line += str(self.lines) + comma
		line += str(self.hit) + comma
		line += str((self.hit*100)/total) + comma
		line += str(self.miss) + comma
		line += str((self.miss*100)/total) + comma
		line += str(self.blockSizeInBits) + comma
		line += str(self.cacheSizeInBits) + comma
		line += str(self._calculateAccessedSamples())
		fp.write(line + "\n")

		
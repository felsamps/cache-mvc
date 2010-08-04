__author__="felsamps"
__date__ ="$03/08/2010 10:28:36$"

class Statistics:
	def __init__(self):
		self.miss = 0
		self.hit = 0

	def addMiss(self):
		self.miss = self.miss + 1

	def addHit(self):
		self.hit = self.hit + 1

	def printStats(self):
		total = self.hit + self.miss
		print "TOTAL ACCESSES:"
		print "HITS:", self.hit, str((self.hit*100)/total)+"%"
		print "MISSES:", self.miss, str((self.miss*100)/total)+"%"
		
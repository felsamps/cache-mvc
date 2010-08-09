__author__="felsamps"
__date__ ="$09/08/2010 08:41:03$"

import sys

from Cache import *
from ConfigFile import *
from MMU import *
from TraceFile import *
from SearchEngine import *

w = 640
h = 480

orders = [0,1,2]
bmas = [["diamond","/home/felsamps/Tcc/cache-mvc/inDiamondTZ.txt"], ["square", "/home/felsamps/Tcc/cache-mvc/inSquareTZ.txt"]]
sets = [1, 2, 3, 4, 5, 6, 7, 8]
blocks = [[16,16], [20,20], [40,40], [32,24], [40, 30]]
caches = [[2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9], [10,10], [3,4], [4,5], [5,6], [3,5]]

stats = []

if __name__ == "__main__":
	i = 1
	total = len(orders) * len(bmas) * len(sets) * len(blocks) * len(caches)
	for order in orders:
		for bma in bmas:
			for set in sets:
				for block in blocks:
					for cache in caches:
						config = ConfigFile("fake")
						config.initConfigs(w, h, block[0], block[1], set, cache[0]*cache[1], cache[0], cache[1], order, bma[0])
						trace = TraceFile(bma[1])
						print "Executando configuracao " , i, "de", total
						engine = SearchEngine(trace, config)
						engine.process()
						stats.append(engine.getStats())
						i += 1

	fp = open("/home/felsamps/Tcc/cache-mvc/results/results.csv","w")
	stats[0].printHeader(fp)
	for result in stats:
		# @type result Stats
		result.reportFile(fp)

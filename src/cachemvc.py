__author__="felsamps"
__date__ ="$16/07/2010 15:27:49$"

from ConfigFile import *
from Cache import *
from ConfigFile import *
from MMU import *

if __name__ == "__main__":
	configFile = ConfigFile("template.cfg")
	mmu = MMU(configFile)
	for i in range(0,configFile.getFrameW(),16):
		for j in range(0,configFile.getFrameH(), 16):
			print i, j
			mmu.performAccess(  i,  j)
			mmu.performAccess(i+1,  j)
			mmu.performAccess(  i,j+1)
			mmu.performAccess(i+1,j+1)
			mmu.performAccess(i-1,  j)
			mmu.performAccess(  i,j-1)
			mmu.performAccess(i-1,j-1)
	mmu.printStats()
	

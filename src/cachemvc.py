__author__="felsamps"
__date__ ="$16/07/2010 15:27:49$"

import sys

from Cache import *
from ConfigFile import *
from MMU import *
from TraceFile import *
from SearchEngine import *


if __name__ == "__main__":
	configFile = ConfigFile(sys.argv[1])
	configFile.parseFile()
	traceFile = TraceFile(sys.argv[2])
	me = SearchEngine(traceFile, configFile)
	me.process()

__author__="felsamps"
__date__ ="$16/07/2010 15:27:49$"

from ConfigFile import *
from Cache import *

if __name__ == "__main__":
	configFile = ConfigFile("template.cfg")
	cache = Cache(configFile)

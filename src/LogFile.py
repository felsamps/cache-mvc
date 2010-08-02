__author__="felsamps"
__date__ ="$02/08/2010 10:59:13$"

class LogFile():
	def __init__(self, name):
		self.fp = open(name,"w")

	def log(self, str):
		self.fp.write(str)

	def close(self):
		self.fp.close()
		
if __name__ == "__main__":
    print "Hello World"

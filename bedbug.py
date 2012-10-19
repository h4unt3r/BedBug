import pdb
import inspect
import collections

import platform
if 'win' in platform.platform().lower():
	from msvcrt import kbhit as getc
else:
	# Some other method of nonblocking read...

class Stream(object):

	def __init__(self, fh):
		self.fh = fh
		self.out = collections.deque()
		self.buffered = false
	
	def toggleBuffered(self):
		self.buffered = not self.buffered

	def write(self, 


class BedBug(object):
	
	def __init__(self):
		self.version = 1
		self.versionString = "1.0 (Itchy)"
		self.debug = False

	def debug(self, shell=True, promt="\nThere ya go:"):
		if not self.debug:
			return
		if prompt:
			print prompt
		if shell:
			print ">>> BedBug - %s <<<" % self.versionString
			print "<<< Type ''\h' for help :P"
			while True:
				cmd = raw_input(">>> ")

name = ""
tree = None
wrapper = None

def classHook(cls):
	import inspect
	global name
	name = cls.__name__
	for item in inspect.getmembers(cls, inspect.ismethod):
		setattr(cls, item[0], wrapper(item[1]))

def writeTree():
	import os
	import commonbug
	fname = os.getcwd() + os.sep  + name
	while os.path.exists(fname + ".dot"):
		fname = commonbug.upLabel(fname)
	fh = open(fname + ".dot", "w")
	tree.toFile(fh)

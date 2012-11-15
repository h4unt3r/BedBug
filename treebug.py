import os
import time
import commonbug

_l = "aaaa"
class TreeNode(object):
	def __init__(self, key):
		global _l
		self.label = _l
		_l = commonbug.upLabel(_l)
		self.write = True
		self.key = key
		self.children = []
		self.time = 0.0
	
	def __repr__(self):
		string = "'<TreeNode \"%s\":[" % self.key
		string += ", ".join([child.key for child in self.children])
		string += "]>'"
		return string

	def __str__(self):
		return self.label
	
	def addNode(self, node):
		if type(node) == str:
			node = TreeNode(node)
		self.children.append(node)
	
	def delNode(self, index):
		self.children.pop(index)
	
	# Needs Werk
	def getTime(self):
		if not self.children:
			return self.time

		# Else sum the times of the children
		self.time = 0.0
		for child in self.children:
			self.time += child.getTime()
		return self.time
	
	#def colorNodes(self, root=True):

	def toFile(self, fh=None, root=True):
		# If we arent set to write...
		if not self.write:
			return

		# In the case the root node is writing...
		if root:
			# If fh is not a file
			if not type(fh) is file:
				# Check that there is a dotdot dir
				path = os.getcwd() + os.sep + ".dot" + os.sep
				if not os.path.exists(path):
					os.mkdir(path)
				# We were passed a filename
				if type(fh) is str:
					if not os.path.exists(fh):
						fname = fh
					else:
						fh = None
				# use a different name if occupied
				if not fh:
					fname = path + self.key
				# Create teh file then!
				fh = open(fname + ".dot", "w")
			# Lastly write the context as root
			fh.write("digraph %s {\n" % self.key)

		# Write the current node and children in...
		fh.write("\t%s [label=\"%s\"];\n" % (self, "%s\\n%d" % (self.key, self.getTime())))
		[fh.write("\t\t%s -> %s;\n" % (self, child)) for child in self.children]

		# Tell the children to write themselves...
		for child in self.children:
			child.toFile(fh, root=False)

		# Finishing as root, clean up
		if root:
			fh.write("}")
			fh.close()

# Our root node
_r = None
def treeit(func):
	def wrapper(*args, **kwargs):
		global _r
		r = _r
		if not r:
			_r = TreeNode(func.__name__)
		# else r is set to the parent
		else:
			_r = TreeNode(func.__name__)
			r.addNode(_r)
		t1 = time.clock()
		ret = func(*args, **kwargs)
		t2 = time.clock()
		if not _r.children:
			_r.time = (t2 - t1) * 1000.0
			print _r.time
		# We are root, write out
		if not r:
			_r.toFile()
		# Restore root
		_r = r
		return ret
	return wrapper

if __name__ == "__main__":
	print os.path.abspath(__file__)

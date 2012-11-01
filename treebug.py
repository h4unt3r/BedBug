import os
import commonbug

_l = "aaaa"
class TreeNode(object):
	def __init__(self, key):
		global _l
		self.label = _l
		_l = commonbug.upLabel(_l)
		self.key = key
		self.children = []
	
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
	
	def toFile(self, fh=None, root=True):
		if root:
			# Create teh file then!
			if not fh:
				fname = os.getcwd() + os.sep + self.key + ".dot"
				if not os.path.exists(fname):
					fh = open(fname, "w")
				else:
					print "Awwww fuck theres another file there!"
					return
			if fh.tell() == 0:
				fh.write("digraph %s {\n" % self.key)

		fh.write("\t%s [label=\"%s\"];\n" % (self, self.key))
		[fh.write("\t\t%s -> %s;\n" % (self, child)) for child in self.children]
		for child in self.children:
			child.toFile(fh, root=False)

		if root:
			fh.write("}")
			fh.close()

# Our root node
_r = TreeNode("__main__")
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
		ret = func(*args, **kwargs)
		# Restore the parent for siblings called
		if r:
			_r = r
		return ret
	return wrapper

if __name__ == "__main__":
	print os.path.abspath(__file__)

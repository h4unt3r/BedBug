name = ""
tree = None
wrapper = None

def classHook(cls):
	import inspect
	global name
	name = cls.__name__
	for item in inspect.getmembers(cls, inspect.ismethod):
		setattr(cls, item[0], wrapper(item[1]))

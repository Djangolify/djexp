import inspect


class Class(object):

	FIELD = 10000

	def __init__(self, cls: object):
		if not inspect.isclass(cls):
			raise ValueError('object \'{}\' is not a class'.format(cls))
		self.__cls = cls

	def __method__(self, m_name: str):
		return self.__cls.__dict__[m_name]

	def name(self):
		return self.__cls.__name__

	def bases(self):
		return self.__cls.__bases__

	def methods(self):
		res = []
		for y in [getattr(self.__cls, x) for x in dir(self.__cls)]:
			if inspect.isfunction(y):
				res.append(y.__name__)
		return res

	def get_method_args(self, method_name: str):
		res = {}
		args = inspect.signature(self.__method__(method_name)).parameters
		for arg in args:
			annotation = args[arg].annotation
			res[arg] = annotation.__name__ if not annotation is inspect._empty else None
		return res

	def method_is_static(self, method_name: str):
		return isinstance(self.__method__(method_name), staticmethod)

	def static_fields(self):
		res = {}
		for x in inspect.getmembers(self.__cls):
			attr = getattr(self.__cls, x[0])
			if not x[0].startswith('__') and not callable(attr) and not isinstance(attr, property):
				res[x[0]] = {'value': x[1], 'type': type(attr).__name__}
		return res

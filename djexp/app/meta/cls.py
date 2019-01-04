import inspect


class Class(object):

	def __init__(self, cls: object):
		if not inspect.isclass(cls):
			raise ValueError('object \'{}\' is not a class'.format(cls))
		self.__cls = cls

	@property
	def name(self):
		return self.__cls.__name__

	@property
	def bases(self):
		return self.__cls.__bases__

	@property
	def static_fields(self):
		res = []
		for x in inspect.getmembers(self.__cls):
			attr = getattr(self.__cls, x[0])
			if not x[0].startswith('__') and not callable(attr) and not isinstance(attr, property):
				res.append({'name': x[0], 'value': x[1], 'type': type(attr).__name__})
		return res

	@property
	def dictionary(self):
		return {
			'name': self.name,
			'fields': self.static_fields
		}

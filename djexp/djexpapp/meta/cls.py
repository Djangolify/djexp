import inspect

from ..normalizer.normalizers import normalize_type


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
		for field in self.__cls._meta.fields:
			normalized_type = normalize_type(type(field))
			if normalized_type is not None:
				res.append({'name': str(field).split('.')[-1], 'type': normalized_type})
		return res

	@staticmethod
	def __is_user_defined_field(field, attr):
		return not field.startswith('__') and \
				not field.startswith('_') and \
				not callable(attr) and \
				not isinstance(attr, property)

	@property
	def dictionary(self):
		return {
			'name': self.name,
			'fields': self.static_fields
		}

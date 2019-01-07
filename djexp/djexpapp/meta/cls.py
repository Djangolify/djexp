import inspect

from ..normalizer.normalizers import normalize_type, normalize_relations


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
			if normalized_type is None:
				normalized_type = normalize_relations(field)
				if normalized_type is None:
					continue
			res.append({'unique': field.unique, 'name': str(field).split('.')[-1], 'type': normalized_type})
		return res

	@property
	def dictionary(self):
		return {
			'name': self.name,
			'fields': self.static_fields
		}

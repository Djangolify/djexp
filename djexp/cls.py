import inspect

from djexp.exceptions import DjexpError
from djexp.normalizer.normalizers import (
	normalize_type,
	module_to_path,
	normalize_relations
)


class Class(object):

	def __init__(self, cls: object):
		if not inspect.isclass(cls):
			raise DjexpError('object \'{}\' is not a class'.format(cls))
		self.__class = cls
		self.__fields_got = False
		self.__static_fields = []
		self.__path = module_to_path(inspect.getmodule(self.__class).__name__)

	@property
	def name(self):
		return self.__class.__name__

	@property
	def bases(self):
		return self.__class.__bases__

	@property
	def path(self):
		return self.__path

	@property
	def static_fields(self):
		if not self.__fields_got:
			for field in self.__class._meta.fields:
				normalized_type = normalize_type(type(field))
				if normalized_type is None:
					normalized_type = normalize_relations(field)
					if normalized_type is None:
						continue
				self.__static_fields.append({
					'unique': field.unique,
					'type': normalized_type,
					'name': str(field).split('.')[-1]
				})
		return self.__static_fields

	@property
	def dictionary(self):
		return {
			'name': self.name,
			'path': self.path,
			'fields': self.static_fields
		}

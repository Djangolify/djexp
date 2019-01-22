import inspect

from djexp.types import TYPES
from djexp.normalizers import (
	module_to_path,
	normalize_relations
)
from djexp.exceptions import DjexpError


class Class:

	def __init__(self, cls):
		if not inspect.isclass(cls):
			raise DjexpError('object \'{}\' is not a class'.format(cls))
		self.__class = cls
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
		static_fields = []
		for field in self.__class._meta.fields:
			if not type(field).__name__ in TYPES.keys():
				normalized_type = normalize_relations(field)
				if normalized_type is None:
					continue
			else:
				normalized_type = TYPES[type(field).__name__]
			static_fields.append({
				'unique': field.unique,
				'type': normalized_type,
				'name': str(field).split('.')[-1]
			})
		return static_fields

	@property
	def dictionary(self):
		return {
			'name': self.name,
			'path': self.path,
			'fields': self.static_fields
		}

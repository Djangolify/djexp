import inspect
from importlib import util

from django.db.models import Model

from .cls import Class


class Module(object):

	def __init__(self, m_name: str, m_path: str):
		spec = util.spec_from_file_location(m_name, m_path)
		self.__module = util.module_from_spec(spec)
		spec.loader.exec_module(self.__module)

	def members(self, predicate=None):
		if predicate is None:
			return inspect.getmembers(self.__module)
		return inspect.getmembers(self.__module, predicate)

	@property
	def classes(self):
		return self.members(inspect.isclass)

	@property
	def dictionary(self):
		classes = [Class(cls[1]) for cls in self.classes]
		final_classes = [cls for cls in classes if Model in cls.bases]
		return {
			'name': self.__module.__name__,
			'classes': [cls.dictionary for cls in final_classes]
		}

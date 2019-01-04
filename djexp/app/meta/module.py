import sys
import inspect

from .cls import Class


class Module(object):

	def __init__(self, m_name: str):
		self.__module = sys.modules[m_name]

	def members(self, predicate=None):
		if predicate is None:
			return inspect.getmembers(self.__module)
		return inspect.getmembers(self.__module, predicate)

	@property
	def classes(self):
		return self.members(inspect.isclass)

	@property
	def dictionary(self):
		classes = [Class(cls) for cls in self.classes]

		# TODO: remove classes that are not Django's Model child

		return {
			'name': self.__module.__name__,
			'classes': [cls.dictionary for cls in classes]
		}

import sys
import inspect


class Module(object):

	def __init__(self, m_name: str):
		self.__module = sys.modules[m_name]

	def members(self, predicate=None):
		if predicate is None:
			return inspect.getmembers(self.__module)
		return inspect.getmembers(self.__module, predicate)

	def classes(self):
		return self.members(inspect.isclass)

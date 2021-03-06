import inspect
from os import environ
from importlib import import_module

import django
from django.db.models import Model

from .cls import Class


class Module(object):

	def __init__(self, m_name: str, settings_module: str):
		environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
		django.setup()
		self.__module = import_module(m_name)
		classes = [Class(cls[1]) for cls in self.members(inspect.isclass) if cls[1].__module__ == self.__module.__name__]
		self.__classes = [cls for cls in classes if Model in cls.bases]

	def members(self, predicate=None):
		if predicate is None:
			return inspect.getmembers(self.__module)
		return inspect.getmembers(self.__module, predicate)

	@property
	def classes(self):
		return self.__classes

	@property
	def dictionary(self):
		return {
			'name': self.__module.__name__,
			'classes': [cls.dictionary for cls in self.classes]
		}

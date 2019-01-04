from unittest import TestCase

from djexp.app.export import normalize_root, get_modules, path_to_module
from djexp.app.meta.module import Module


class TestExport(TestCase):

	def test_normalize_root(self):
		data = [
			('./root/folder/', './root/folder'),
			('root/folder/', 'root/folder'),
			('.//root////////folder//////', './root/folder')
		]
		for d in data:
			self.assertEqual(normalize_root(d[0]), d[1])

	def test_path_to_module(self):
		data = [
			('./root/folder/', 'root.folder'),
			('root/folder/', 'root.folder'),
			('.//root////////folder//////', 'root.folder')
		]
		for d in data:
			self.assertEqual(path_to_module(d[0]), d[1])

	def test_get_modules(self):
		expected = [
			'tests.test_export', 'tests.test_meta.test_module',
			'tests.test_meta.demo_module', 'tests.test_meta.test_cls',
		]
		actual = get_modules('../tests')
	#	for i in range(len(expected)):
	#		self.assertEqual(expected[i], actual[i])
		print([Module('djexp.{}'.format(x)) for x in actual])

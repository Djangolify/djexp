from unittest import TestCase

from djexpapp.export import normalize_root, path_to_module


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
			('./root/folder/module.py', 'root.folder.module'),
			('root/folder/module.py', 'root.folder.module'),
			('.//root////////folder//////module.py', 'root.folder.module')
		]
		for d in data:
			self.assertEqual(path_to_module(d[0]), d[1])

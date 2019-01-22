from unittest import TestCase

from djexp.export import normalize_root
from djexp.normalizers import module_to_path


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
			('root.folder.module_name', 'root/folder'),
		]
		for d in data:
			self.assertEqual(module_to_path(d[0]), d[1])

from unittest import TestCase

from djexp.export import normalize_root
from djexp.utils import get_module_path


class TestUtils(TestCase):

	def test_normalize_root(self):
		data = [
			('./root/folder/', './root/folder'),
			('root/folder/', 'root/folder'),
			('.//root////////folder//////', './root/folder'),
			('..//root////////folder//////', '../root/folder'),
			('...//root////////folder//////', '../root/folder'),
		]
		for d in data:
			self.assertEqual(normalize_root(d[0]), d[1])

	def test_get_module_dir(self):
		data = [
			('root.folder.module_name', 'root/folder/module_name'),
			('module_name', 'module_name'),
			('root.module_name', 'root/module_name'),
			('..root.module_name', '../root/module_name')
		]
		for d in data:
			self.assertEqual(get_module_path(d[0]), d[1])

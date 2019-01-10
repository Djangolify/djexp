from unittest import TestCase

from djexp.meta.module import Module


class TestModule(TestCase):

	def setUp(self):
		self.module = Module('tests.test_meta.demo_module', './test_meta/demo_module.py')

from unittest import TestCase

from djexpapp.meta.module import Module


class TestModule(TestCase):

	def setUp(self):
		self.module = Module('djexp.tests.test_meta.demo_module', './test_meta/demo_module.py')

from unittest import TestCase

from djexp.app.meta.module import Module
from djexp.tests.test_meta.demo_module import TestClass, AnotherTestClass


class TestModule(TestCase):

	def setUp(self):
		self.module = Module('djexp.tests.test_meta.demo_module', './test_meta/demo_module.py')

	def test_classes(self):
		actual = self.module.classes
		expected = [
			('AnotherTestClass', AnotherTestClass),
			('TestClass', TestClass)
		]
		self.assertEqual(len(actual), len(expected))
		for i in range(len(expected)):
			self.assertEqual(isinstance(expected[i], tuple), isinstance(actual[i], tuple))

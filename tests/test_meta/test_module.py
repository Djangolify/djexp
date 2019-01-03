from unittest import TestCase

from pyexport.meta.module import Module
from tests.test_meta.demo_module import TestClass, AnotherTestClass


class TestModule(TestCase):

	def setUp(self):
		self.module = Module('tests.test_meta.demo_module')

	def test_classes(self):
		actual = self.module.classes
		expected = [
			('AnotherTestClass', AnotherTestClass),
			('TestClass', TestClass)
		]
		self.assertEqual(len(actual), len(expected))
		for i in range(len(expected)):
			self.assertEqual(isinstance(expected[i], tuple), isinstance(actual[i], tuple))
			self.assertEqual(expected[i][0], actual[i][0])
			self.assertEqual(expected[i][1], actual[i][1])

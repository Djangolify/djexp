from unittest import TestCase

from djexp.meta.cls import Class
from tests.test_meta.demo_module import TestClass, AnotherTestClass


class TestCls(TestCase):

	def setUp(self):
		self.cls = Class(TestClass)

	def test_name(self):
		self.assertEqual(self.cls.name, 'TestClass')

	def test_bases(self):
		cls = Class(AnotherTestClass)
		self.assertTrue(str in cls.bases and TestClass in cls.bases)


"""
	def test_static_fields(self):
		actual = self.cls.static_fields
		expected = [
			{
				'name': 'FLOAT_FIELD',
				'value': 10000000000.100000000000000001,
				'type': 'float'
			},
			{
				'name': 'INT_STATIC_FIELD',
				'value': 1000000000000000000000000000000000000,
				'type': 'int'
			},
			{
				'name': 'STR_STATIC',
				'value': 'this is string static field',
				'type': 'str'
			}
		]
		self.assertEqual(isinstance(actual, list), isinstance(expected, list))
		for i in range(len(expected)):
			self.assertEqual(actual[i]['name'], expected[i]['name'])
			self.assertEqual(actual[i]['value'], expected[i]['value'])
			self.assertEqual(actual[i]['type'], expected[i]['type'])
"""

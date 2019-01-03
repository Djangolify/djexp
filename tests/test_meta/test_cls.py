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

	def test_methods(self):
		actual = self.cls.methods
		expected = ['method_with_args', 'some_method', 'this_is_static_method']
		self.assertEqual(len(actual), len(expected))
		for i in range(len(actual)):
			self.assertEqual(actual[i], expected[i])

	def test_static_fields(self):
		actual = self.cls.static_fields
		expected = {
			'FLOAT_FIELD': {
				'value': 10000000000.100000000000000001,
				'type': 'float'
			},
			'INT_STATIC_FIELD': {
				'value': 1000000000000000000000000000000000000,
				'type': 'int'
			},
			'STR_STATIC': {
				'value': 'this is string static field',
				'type': 'str'
			}
		}
		self.assertEqual(isinstance(actual, dict), isinstance(expected, dict))
		for key, value in expected.items():
			self.assertEqual(actual[key]['value'], value['value'])
			self.assertEqual(actual[key]['type'], value['type'])

	def test_get_method_args(self):
		expected = {
			'self': None,
			'arg1': 'str',
			'arg2': None,
			'arg3': 'int'
		}
		actual = self.cls.get_method_args('method_with_args')
		self.assertEqual(len(actual), len(expected))
		for key, value in expected.items():
			self.assertEqual(actual[key], expected[key])

	def test_method_is_static(self):
		self.assertTrue(self.cls.method_is_static('this_is_static_method'))
		self.assertFalse(self.cls.method_is_static('some_method'))

	def test___method__(self):
		self.assertRaises(KeyError, self.cls.__method__, ('this_is_static_method_1',))
		self.assertEqual(self.cls.__method__('method_with_args'), TestClass.method_with_args)

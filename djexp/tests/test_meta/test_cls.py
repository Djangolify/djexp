from unittest import TestCase

from djexp.app.meta.cls import Class
from djexp.tests.test_meta.demo_module import TestClass, AnotherTestClass


class TestCls(TestCase):

	def setUp(self):
		self.cls = Class(TestClass)

	def test_name(self):
		self.assertEqual(self.cls.name, 'TestClass')

	def test_bases(self):
		cls = Class(AnotherTestClass)
		self.assertTrue(str in cls.bases and TestClass in cls.bases)

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

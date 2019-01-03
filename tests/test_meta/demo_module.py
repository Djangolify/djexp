class TestClass(object):

	INT_STATIC_FIELD = 1000000000000000000000000000000000000
	STR_STATIC = 'this is string static field'
	FLOAT_FIELD = 10000000000.100000000000000001

	def some_method(self):
		pass

	def method_with_args(self, arg1: str, arg2, arg3: int):
		pass

	@staticmethod
	def this_is_static_method():
		pass


class AnotherTestClass(str, TestClass):
	pass

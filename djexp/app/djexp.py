import sys

from .__version__ import __version__


def main():
	print('Executing \'djexp\' version {}.'.format(__version__))
	print('List of argument strings: {}'.format(sys.argv[1:]))

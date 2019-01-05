import sys

from .export import export


def cli_exec():
	print('Exporting...')
	export(sys.argv[1])
	print('Done.')

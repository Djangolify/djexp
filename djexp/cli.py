import os
import sys
import argparse

import django

from djexp import (
	__version__,
	__app_name__,
	__description__
)
from djexp.export import export
from djexp.exceptions import DjexpCliError


def arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-r', '--root', help='project root directory', default='./')
	parser.add_argument('-s', '--settings', help='project settings module')
	parser.add_argument('-v', '--version', action='store_true', default=False, help='check app version')
	parser.add_argument('--yml', '--yaml', action='store_true', default=False, help='output to yaml file format')
	parser.add_argument('--json', action='store_true', default=True, help='output to json file format')
	return parser


def exec_export(args, file_format):
	print('Exporting...')
	sys.path.append(args.root)
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', args.settings)
	django.setup()
	export(**{
		'root_dir': args.root,
		'file_format': file_format
	})


def cli_exec():
	args = arg_parser().parse_args()
	if args.version:
		print('{}, version {}\n{}'.format(__app_name__, __version__, __description__))
		return
	if args.settings is None:
		print('{}: need to setup settings module\nUse -h, --help for usage info'.format(__app_name__))
		return
	file_format = 'json'
	if args.yml:
		file_format = 'yml'
	try:
		exec_export(args, file_format)
	except DjexpCliError as val_err:
		print('{}: {}, try \'-h\' for help'.format(__app_name__, val_err))

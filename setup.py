#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup, find_packages

from djexp import NAME, DESCRIPTION, VERSION

URL = 'https://github.com/Djangolify/djexp'
EMAIL = 'yuralisovskiy98@gmail.com'
AUTHOR = 'Yuriy Lisovskiy'
REQUIRES_PYTHON = '>=3.6.0'

REQUIRED = ['django>=1.7', 'pyyaml>=4.2b4']

try:
	with io.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
		long_description = '\n' + f.read()
except FileNotFoundError:
	long_description = DESCRIPTION

setup(
	name=NAME,
	version=VERSION,
	description=DESCRIPTION,
	entry_points={
		'console_scripts': ['{} = {}.{}:main'.format(NAME, NAME, NAME)]
	},
	long_description=long_description,
	long_description_content_type='text/markdown',
	author=AUTHOR,
	author_email=EMAIL,
	python_requires=REQUIRES_PYTHON,
	url=URL,
	packages=find_packages(exclude=('tests',)),
	install_requires=REQUIRED,
	include_package_data=True,
	license='GPLv3',
	classifiers=[
		# Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft :: Windows :: Windows 10'
	]
)

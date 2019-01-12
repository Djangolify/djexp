import os
import re


def dir_is_omitted(path_str: str):
	for item in ['__pycache__', 'venv', 'migrations']:
		if item in path_str:
			return True
	return False


def file_id_omitted(file_path: str):
	return not re.search('__.+__.py', file_path) and file_path.endswith('.py') and 'setup.py' not in file_path


def is_valid_module(str_path: str):
	return os.path.isfile(str_path) and file_id_omitted(str_path)

from re import sub
from json import dump
from os import path, makedirs, listdir

from .meta.module import Module

OUTPUT_FILE = 'django-models.json'


def normalize_root(root: str):
	root = sub(r'[^\w.]{2,}', '/', root)
	return root.rstrip('/')


def path_to_module(path_str: str):
	return sub(r'[^\w]+', '.', path_str).rstrip('.py').lstrip('/.')


def save_dict(data: dict, root_path: str):
	root_path = normalize_root(root_path)
	if not path.exists(root_path):
		makedirs(root_path)
	with open('{}/{}'.format(root_path, OUTPUT_FILE), 'w') as f:
		dump(data, f, ensure_ascii=False)


def get_modules(root: str):
	modules = []
	root = normalize_root(root)
	if not path.exists('{}/__init__.py'.format(root)):
		return modules
	for f in listdir(root):
		new_path = path.join(root, f)
		if path.isfile(new_path):
			modules.append(path_to_module(new_path))
		elif '__pycache__' not in new_path:
			modules += get_modules(new_path)
	return modules


def compose_module_data(module: Module):
	pass


def compose_output_data(modules: []):
	pass

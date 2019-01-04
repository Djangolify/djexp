from re import sub, search
from json import dump
from os import path, makedirs, listdir

from .meta.cls import Class
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


def path_id_valid(str_path: str):
	return path.isfile(str_path) and not search('__.+__.py', str_path) and str_path.endswith('.py')


def get_modules(root: str):
	modules = []
	root = normalize_root(root)
	if not path.exists('{}/__init__.py'.format(root)):
		return modules
	for f in listdir(root):
		new_path = path.join(root, f)
		if path_id_valid(new_path):
			modules.append(path_to_module(new_path))
		elif '__pycache__' not in new_path:
			modules += get_modules(new_path)
	return modules


def prepare_modules(module_names: []):
	root_dir_name = 'djexp'    # TODO: find actual root dir name

	return [Module('{}.{}'.format(root_dir_name, x)) for x in module_names]


def compose_output_data(root_dir: str, modules: []):
	return {
		'root': root_dir,
		'count': len(modules),
		'modules': [
			module.dictionary for module in modules
		]
	}


def export(root_dir: str):
	try:
		modules = prepare_modules(get_modules(root_dir))
	except Exception as exc:
		raise Exception('Error occurred while getting modules\' information: {}'.format(exc))
	try:
		out_data = compose_output_data(root_dir, modules)
	except Exception as exc:
		raise Exception('Error occurred while composing output data: {}'.format(exc))
	try:
		save_dict(out_data, root_dir)
	except Exception as exc:
		raise Exception('Error occurred while json data: {}'.format(exc))

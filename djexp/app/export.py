from json import dump
from re import sub, search
from os import path, makedirs, listdir, getcwd

from .meta.module import Module

OUTPUT_FILE = 'django-models.json'


def normalize_root(root: str):
	root = sub(r'[^\w.]{2,}', '/', root)
	return root.rstrip('/')


def path_to_module(path_str: str):
	if path_str.endswith('.py'):
		path_str = path_str[:len(path_str) - 3]
	return sub(r'[^\w]+', '.', path_str).lstrip('/.')


def save_dict(data: dict, root_path: str):
	root_path = normalize_root(root_path)
	if not path.exists(root_path):
		makedirs(root_path)
	with open('{}/{}'.format(root_path, OUTPUT_FILE), 'w') as f:
		dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)


def is_valid_module(str_path: str):
	return path.isfile(str_path) and not search('__.+__.py', str_path) and str_path.endswith(
		'.py') and 'setup.py' not in str_path


def get_modules(root: str):
	modules = []
	root = normalize_root(root)
	for f in listdir(root):
		new_path = path.join(root, f)
		if is_valid_module(new_path):
			modules.append((path_to_module(new_path), new_path))
		elif '__pycache__' not in new_path:
			modules += get_modules(new_path)
	return modules


def prepare_modules(module_names: []):
	# root_dir_name = path.abspath(root_dir).split('/')[-1]
	modules = []
	for x in module_names:
		try:
			modules.append(Module('{}'.format(x[0]), x[1]))
		except ModuleNotFoundError as _:
			pass
	return modules


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
		pass
		out_data = compose_output_data(path.abspath(root_dir), modules)
	except Exception as exc:
		raise Exception('Error occurred while composing output data: {}'.format(exc))
	try:
		pass
		save_dict(out_data, getcwd())
	except Exception as exc:
		raise Exception('Error occurred while json data: {}'.format(exc))

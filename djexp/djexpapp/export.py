import sys
from json import dump
from re import sub, search
from os import path, makedirs, listdir, getcwd

from .meta.module import Module
from djexpapp.normalizer.normalizers import normalize_root

OUTPUT_FILE = 'django-models.json'


def dir_is_omitted(path_str: str):
	for item in ['__pycache__', 'venv', 'migrations']:
		if item in path_str:
			return True
	return False


def file_id_omitted(file_path: str):
	return not search('__.+__.py', file_path) and file_path.endswith('.py') and 'setup.py' not in file_path


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
	return path.isfile(str_path) and file_id_omitted(str_path)


def get_modules(root: str):
	modules = []
	root = normalize_root(root)
	for f in listdir(root):
		new_path = path.join(root, f)
		if is_valid_module(new_path):
			modules.append((path_to_module(new_path), new_path))
		elif path.isdir(new_path) and not dir_is_omitted(new_path):
			modules += get_modules(new_path)
	return modules


def prepare_modules(module_names: [], settings_module: str):
	modules = []
	for x in module_names:
		try:
			modules.append(Module('{}'.format(x[0]), settings_module))
		except ModuleNotFoundError as _:
			pass
	return modules


def compose_output_data(root_dir: str, modules: []):
	final_modules = [module.dictionary for module in modules if len(module.classes) > 0]
	return {
		'root': root_dir,
		'count': len(final_modules),
		'modules': final_modules
	}


def export(root_dir: str, settings_module: str):
	sys.path.append(root_dir)
	try:
		modules = prepare_modules(get_modules(root_dir), settings_module)
	except Exception as exc:
		raise Exception('Error occurred while getting modules\' information: {}'.format(exc))
	try:
		out_data = compose_output_data(path.abspath(root_dir), modules)
	except Exception as exc:
		print(exc)
		raise Exception('Error occurred while composing output data: {}'.format(exc))
	try:
		save_dict(out_data, getcwd())
	except Exception as exc:
		raise Exception('Error occurred while json data: {}'.format(exc))

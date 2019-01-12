import re
import os
import sys
import json
import yaml

from .meta.module import Module
from .normalizer.normalizers import normalize_root

from .validators import is_valid_module, dir_is_omitted

OUTPUT_FILE = 'django-models'


def path_to_module(path_str: str):
	if path_str.endswith('.py'):
		path_str = path_str[:len(path_str) - 3]
	return re.sub(r'[^\w]+', '.', path_str).lstrip('/.')


def save_json(data: dict, target_path: str):
	target_path = '{}.json'.format(target_path)
	with open(target_path, 'w') as f:
		json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
		return target_path


def save_yaml(data: dict, target_path: str):
	target_path = '{}.yml'.format(target_path)
	with open(target_path, 'w') as f:
		yaml.dump(data, f)
		return target_path


def save_dict(data: dict, root_path: str, file_format: str):
	root_path = normalize_root(root_path)
	if not os.path.exists(root_path):
		os.makedirs(root_path)
	target_path = '{}/{}'.format(root_path, OUTPUT_FILE)
	if file_format is 'json':
		return save_json(data, target_path)
	elif file_format is 'yml':
		return save_yaml(data, target_path)
	else:
		raise ValueError('invalid serialization file type')


def get_modules(root: str):
	modules = []
	root = normalize_root(root)
	for f in os.listdir(root):
		new_path = os.path.join(root, f)
		if is_valid_module(new_path):
			modules.append((path_to_module(new_path), new_path))
		elif os.path.isdir(new_path) and not dir_is_omitted(new_path):
			modules += get_modules(new_path)
	return modules


def prepare_modules(module_names: [], settings_module):
	modules = []
	for x in module_names:
		try:
			modules.append(Module('{}'.format(x[0]), settings_module))
		except ModuleNotFoundError as _:
			pass
	return modules


def compose_output_data(root_dir: str, modules: []):
	final_modules = [module.dictionary for module in modules if len(module.classes) > 0]
	return ({
		'root': root_dir,
		'count': len(final_modules),
		'modules': final_modules
	}, len(final_modules))


def export(root_dir: str, settings_module, file_format: str):
	sys.path.append(root_dir)
	try:
		modules = prepare_modules(get_modules(root_dir), settings_module)
	except Exception as exc:
		raise Exception('Error occurred while getting modules\' information: {}'.format(exc))
	if len(modules) > 0:
		try:
			out_data, classes_count = compose_output_data(os.path.abspath(root_dir), modules)
		except Exception as exc:
			print(exc)
			raise Exception('Error occurred while composing output data: {}'.format(exc))
		try:
			saved_path = save_dict(out_data, os.getcwd(), file_format)
		except Exception as exc:
			raise Exception('Error occurred while json data: {}'.format(exc))
		print('Exported {} classes, check out \'{}\' file.'.format(classes_count, saved_path))
	else:
		print('Nothing to export.')

import os
import json
import yaml

import django
from django.apps import apps

from djexp.cls import Class
from djexp.exceptions import DjexpError
from djexp.normalizer.normalizers import normalize_root

OUTPUT_FILE = 'django-models'


def to_classes(classes: []):
	return [Class(cls) for cls in classes]


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
		raise DjexpError('invalid serialization file type')


def compose_output_data(root_dir: str, classes: []):
	if len(classes) > 0:
		res_classes = [cls.dictionary for cls in classes if 'django.contrib' not in cls.path]
		res_count = len(res_classes)
		return ({
			'root': root_dir,
			'count': res_count,
			'classes': res_classes
		}, res_count)
	print('Nothing to export.')
	return None


def export(root_dir: str, file_format: str, settings_module=None):
	try:
		if settings_module is not None:
			os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
			django.setup()
		out_data, classes_count = compose_output_data(
			os.path.abspath(root_dir), to_classes(apps.get_models())
		)
		saved_path = save_dict(out_data, os.getcwd(), file_format)
		print('Exported {} classes, check out \'{}\' file.'.format(classes_count, saved_path))
	except DjexpError as exc:
		print('djexp: {}'.format(exc))

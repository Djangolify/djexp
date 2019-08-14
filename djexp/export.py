import os
import json
import yaml

from django.apps import apps
from django.conf import settings

from djexp import __app_name__
from djexp.model import Model
from djexp.exceptions import DjexpError
from djexp.utils import normalize_root
from djexp.default import IGNORED_DEFAULT, OUTPUT_FILE


def to_models(classes: []):
	return [Model(cls) for cls in classes]


def write_to_file(data: dict, dump, target_path: str, ext: str):
	target_path = '{}.{}'.format(target_path, ext)
	with open(target_path, 'w') as f:
		dump(data, f)
		return target_path


def save_json(data: dict, target_path: str):
	return write_to_file(
		data,
		lambda d, f: json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True),
		target_path,
		'json'
	)


def save_yaml(data: dict, target_path: str):
	return write_to_file(
		data,
		lambda d, f: yaml.dump(data, f),
		target_path,
		'yml'
	)


def save_data(data: dict, root_path: str, file_format: str):
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
		res_classes = [cls.dictionary for cls in classes]
		return ({
			'root': root_dir,
			'classes': res_classes
		}, len(res_classes))
	print('Nothing to export.')
	return None


def filter_models(models: list, ignored: list):
	return [model for model in models if '{}.{}'.format(model.__module__, model.__name__) not in ignored]


def export_models(root_dir: str, ignored):
	models = filter_models(apps.get_models(), ignored)
	out_data, classes_count = compose_output_data(
		os.path.abspath(root_dir), to_models(models)
	)
	return out_data, classes_count


def export(root_dir: str, file_format: str):
	DJEXP_IGNORE = getattr(settings, 'DJEXP_IGNORE', IGNORED_DEFAULT)

	print(DJEXP_IGNORE)

	if 'MODELS' not in DJEXP_IGNORE:
		DJEXP_IGNORE['MODELS'] = []
	try:
		out_data, classes_count = export_models(root_dir, DJEXP_IGNORE['MODELS'])
		saved_path = save_data(out_data, os.getcwd(), file_format)
		print('Exported {} classes, check out \'{}\' file.'.format(classes_count, saved_path))
	except DjexpError as exc:
		print('{}: {}'.format(__app_name__, exc))

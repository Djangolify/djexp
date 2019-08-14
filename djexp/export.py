import os
import json
import yaml
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

from django.apps import apps
from django.conf import settings

from djexp import __app_name__
from djexp.model import Model
from djexp.exceptions import DjexpError
from djexp.utils import normalize_root
from djexp.default import IGNORED_DEFAULT, OUTPUT_FILE


def to_models(classes: []):
	return [Model(cls) for cls in classes]


def _save(data: dict, dump, target_path: str, ext: str):
	target_path = '{}.{}'.format(target_path, ext)
	with open(target_path, 'w') as f:
		dump(data, f)
		return target_path


def save_json(data: dict, target_path: str):
	return _save(
		data,
		lambda d, f: json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True),
		target_path,
		'json'
	)


def save_yaml(data: dict, target_path: str):
	return _save(data, lambda d, f: yaml.dump(data, f), target_path, 'yml')


def save_xml(data: dict, target_path: str):
	def dump(d, f):
		xml = dicttoxml(d, custom_root=d.get('root').split('/')[-1], attr_type=False)
		f.write(parseString(xml).toprettyxml(encoding='utf-8').decode('utf-8'))
	return _save(data, dump, target_path, 'xml')


def save_data(data: dict, root_path: str, file_format: str):
	root_path = normalize_root(root_path)
	if not os.path.exists(root_path):
		os.makedirs(root_path)
	target_path = '{}/{}'.format(root_path, OUTPUT_FILE)
	if file_format is 'json':
		return save_json(data, target_path)
	elif file_format is 'yml':
		return save_yaml(data, target_path)
	elif file_format is 'xml':
		return save_xml(data, target_path)
	else:
		raise DjexpError('\'{}\' format is not supported'.format(file_format))


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
	if 'MODELS' not in DJEXP_IGNORE:
		DJEXP_IGNORE['MODELS'] = []
	try:
		out_data, classes_count = export_models(root_dir, DJEXP_IGNORE['MODELS'])
		saved_path = save_data(out_data, os.getcwd(), file_format)
		print('Exported {} classes, check out \'{}\' file.'.format(classes_count, saved_path))
	except DjexpError as exc:
		print('{}: {}'.format(__app_name__, exc))

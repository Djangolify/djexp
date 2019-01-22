import re

import django
from django.db import models


def normalize_root(root: str):
	root = re.sub(r'[^\w.]{2,}', '/', root)
	return root.rstrip('/')


def module_to_path(path_str: str):
	last = path_str.rfind('.')
	if last is not -1:
		path_str = path_str[:last]
	return path_str.replace('.', '/')


def get_rel_model(field):
	if django.__version__ < '2.0':
		return field.rel.to
	else:
		return field.remote_field.model


def normalize_relations(field):
	field_type = type(field)
	if field_type is models.ForeignKey:
		return 'ForeignKey({})'.format(get_rel_model(field).__name__)
	if field_type is models.ManyToManyField:
		return 'ManyToManyField({})'.format(get_rel_model(field).__name__)
	if field_type is models.OneToOneField:
		return 'OneToOneField({})'.format(get_rel_model(field).__name__)
	return None

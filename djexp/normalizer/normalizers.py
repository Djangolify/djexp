import re

import django
from django.db import models

from djexp.normalizer.django_types import (
	STR_TYPES,
	TIME_TYPES,
	BYTE_TYPES,
	BOOL_TYPES,
	INT32_TYPES,
	INT64_TYPES,
	UINT64_TYPES,
	UINT32_TYPES,
	FLOAT64_TYPES
)


def normalize_root(root: str):
	root = re.sub(r'[^\w.]{2,}', '/', root)
	return root.rstrip('/')


def module_to_path(path_str: str):
	last = path_str.rfind('.')
	if last is not -1:
		path_str = path_str[:last]
	return path_str.replace('.', '/')


def normalize_type(data_type):
	if data_type.__name__ in STR_TYPES:
		return 'string'
	if data_type.__name__ in TIME_TYPES:
		return 'time'
	if data_type.__name__ in BYTE_TYPES:
		return '[]byte'
	if data_type.__name__ in BOOL_TYPES:
		return 'bool'
	if data_type.__name__ in INT32_TYPES:
		return 'int32'
	if data_type.__name__ in INT64_TYPES:
		return 'int64'
	if data_type.__name__ in UINT64_TYPES:
		return 'uint64'
	if data_type.__name__ in UINT32_TYPES:
		return 'uint32'
	if data_type.__name__ in FLOAT64_TYPES:
		return 'float64'
	return None


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

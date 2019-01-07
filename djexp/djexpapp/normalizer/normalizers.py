from re import sub

from .django_types import (
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
	root = sub(r'[^\w.]{2,}', '/', root)
	return root.rstrip('/')


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

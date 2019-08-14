import django
from re import sub, search
from djexp.types import RELATION_TYPES


def normalize_root(root: str):
	root = sub('[.]{3,}', '..', sub(r'[/\\]{2,}', '/', root))
	return root.rstrip('/')


def get_module_path(path_str: str):
	match = search('(\\.{2,}).*', path_str)
	pref = ''
	if match:
		path_str = path_str.strip('.')
		pref = '{}/'.format(match.group(1))
	parts = path_str.split('.')
	return pref + ('/'.join(parts))


def get_rel_model(field):
	if django.__version__ < '2.0':
		return field.rel.to
	else:
		return field.remote_field.model


def normalize_relations(field):
	field_type = type(field)

	if field_type in RELATION_TYPES.keys():
		return RELATION_TYPES[field_type].format(get_rel_model(field).__name__)
	return None

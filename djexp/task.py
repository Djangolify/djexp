from djexp.export import export


def export_django_models(root: str, settings_module, file_format: str = 'json'):
	print('Exporting...')
	export(root, settings_module, file_format)

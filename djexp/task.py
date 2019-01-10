from djexp.export import export


def export_django_models(root: str, settings_module: str, file_format: str = None):
	if file_format:
		export(root, settings_module, file_format)
	export(root, settings_module)

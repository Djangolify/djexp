from djexpapp.export import export


def export_django_models(root: str, settings_module: str):
	export(root, settings_module)


# Result file's name
OUTPUT_FILE = 'django-project'

# Django's built-in models
IGNORED_MODELS = [
	'django.contrib.admin.models.LogEntry',
	'django.contrib.auth.models.Permission',
	'django.contrib.auth.models.Group',
	'django.contrib.contenttypes.models.ContentType',
	'django.contrib.sessions.models.Session'
]

# Default djexp setting
IGNORED_DEFAULT = {
	'MODELS': IGNORED_MODELS
}

# Default export formats.
#
# Available output file formats:
# - json
# - yml
# - xml
FORMATS_DEFAULT = [
	'json'
]

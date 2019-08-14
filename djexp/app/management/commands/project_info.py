from djexp.export import export
from djexp.default import FORMATS_DEFAULT

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

	def handle(self, **options):
		DJEXP_FORMATS = getattr(settings, 'DJEXP_FORMATS', FORMATS_DEFAULT)
		for file_format in DJEXP_FORMATS:
			print('\nExporting to \'{}\'...'.format(file_format))
			export(settings.BASE_DIR, file_format)

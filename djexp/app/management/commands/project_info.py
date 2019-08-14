from djexp.export import export

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):

	def handle(self, **options):
		print('Exporting...')
		export(settings.BASE_DIR, 'json')

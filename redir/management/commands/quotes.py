from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from redir.tasks import generate_json_quotes


class Command(BaseCommand):
    help = 'Quote site tasks.'

    def add_arguments(self, parser):
        parser.add_argument('--all', action='store_true', dest='all', default=True, help='Do all for quotes.')

    def handle(self, *args, **options):
        if options['all']:
            generate_json_quotes()

            self.stdout.write(self.style.SUCCESS('Successfully done jobs.'))

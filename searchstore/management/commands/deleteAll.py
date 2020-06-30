from django.core.management.base import BaseCommand
from searchstore.admin import *
from searchstore.models import *


class Command(BaseCommand):
    # help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):

        crawledData.objects.all().delete()

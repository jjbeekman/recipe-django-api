"""
Django command to wait for DB
"""

import time
from psycopg2 import OperationalError as Psychopg2Error
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for DB"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, Psychopg2Error):
                self.stdout.write("DB unavailable. Waiting one second...")
                time.sleep(1)

        self.stdout.write("DB is up!")

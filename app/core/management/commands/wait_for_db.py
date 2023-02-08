# Django coomand to wait for database to be available.

import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    # Django Command to wait for DB

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Databases unablailable ,waiting 1 sec...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database avilable!"))

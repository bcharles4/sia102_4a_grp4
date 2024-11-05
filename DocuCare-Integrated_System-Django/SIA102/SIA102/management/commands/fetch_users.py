import time
from django.core.management.base import BaseCommand
from SIA102.views import fetch_users_data  # Import your fetch function

class Command(BaseCommand):
    help = "Fetches users data from external API every 10 minutes"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting fetch_users task...")
        while True:
            fetch_users_data()  # Call your function
            self.stdout.write("Fetched users data successfully.")
            time.sleep(10)  # Wait 10 seconds before running again

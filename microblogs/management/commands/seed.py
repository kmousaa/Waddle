from django.core.management.base import BaseCommand, CommandError
from faker import Faker
# faker can generate firstname and lastname in text

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    # add seed command (generate 100 random users)
    # remove all regular users (but dont remove superuser and staff acc)
    def handle(self, *args, **options):
        print("WARNING: the seed command is not implemented ")

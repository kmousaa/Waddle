from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

import random
import string

letters = string.ascii_lowercase


# faker can generate firstname and lastname in text

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    # add seed command (generate 100 random users)
    # remove all regular users (but dont remove superuser and staff acc)
    def handle(self, *args, **options):

        for i in range(100):

            fname = self.faker.first_name()
            lname = self.faker.last_name()

            mails = ["gmail.com","yahoo.com","outlook.com","icloud.com.com"]
            passw = ''.join(random.choice(letters) for i in range(10))

            obj = User.objects.create_user(
            username = f"{fname}{lname}{random.randint(0,999)}",
             first_name = fname,
             last_name = lname,
             email = f'{fname[0].lower()}{lname.lower()}@{mails[random.randint(0,3)]}',
             password = f'{passw}',
             bio = self.faker.sentence()

             )

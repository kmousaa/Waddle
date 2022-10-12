from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User




class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        for i in range(len(users)):

            if users[i].username != "@admin":
                users[i].delete()

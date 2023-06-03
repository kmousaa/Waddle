from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User, Post




class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        for i in range(len(users)):

            if users[i].username != "@admin123":
                users[i].delete()
      
        posts = Post.objects.all()
        for i in range(len(posts)):
            posts[i].delete()
            

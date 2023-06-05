from django.core.validators import RegexValidator
from django.db import models
from libgravatar import Gravatar
# Create your models here.

from django.contrib.auth.models  import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length = 30,
        unique = True,
        validators=[RegexValidator(
            regex= r'^@\w{3,}$',
            message='Username must consist of @ symbol followed by at least 3 alphanumericals'
        ) ]
    )

    first_name = models.CharField(
        blank = False,
        unique = False,
        max_length = 50
    )

    last_name = models.CharField(
        blank = False,
        unique = False,
        max_length = 50
    )

    email = models.EmailField(
        unique = True,
        blank = False

    )
    bio = models.CharField(
        max_length = 160 ,
        blank = True
    )

    follows = models.ManyToManyField(
        "self", 
        related_name = "user_follows"
    )

    

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)
    # his method can generate a URL to an image containing the user's gravatar
    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url



class Post(models.Model):

    author = models.ForeignKey('User', null=True,on_delete=models.SET_NULL)

    text = models.CharField(
        max_length = 280
    )
    created_at = models.DateTimeField(
         auto_now_add=True
    )

    # user can like many posts, and post can have many likes
    likes = models.ManyToManyField(
        User, 
        related_name = "user_post"
    )
    


    def total_likes(self):
        return self.likes.count()

    class Meta:
         ordering = ["created_at"]

from django.core.validators import RegexValidator
from django.db import models

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
        max_length = 520 ,
        blank = True
    )

class Post(models.Model):
    author = models.ForeignKey('User', null=True,on_delete=models.SET_NULL)

    text = models.CharField(
        max_length = 280
    )
    created_at = models.DateTimeField(
         auto_now_add=True
    )
    class Meta:
         ordering = ["created_at"]

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    userIdnumber = models.CharField(max_length=20, unique=True, null=False)

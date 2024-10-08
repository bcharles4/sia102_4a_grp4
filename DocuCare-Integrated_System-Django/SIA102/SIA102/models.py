from django.db import models
from django.contrib.auth.hashers import make_password

class Nurse(models.Model):
    userIdnumber = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.userIdnumber})'

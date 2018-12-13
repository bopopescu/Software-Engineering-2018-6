from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    registration_date = models.DateTimeField('Registration date', auto_now=True)


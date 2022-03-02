from statistics import mode
from django.db import models
# from django.contrib.auth.models import AbstractUser


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

# class User(AbstractUser):
#     pass
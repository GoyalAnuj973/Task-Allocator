from statistics import mode
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


# from django.contrib.auth import get_user_model
# User = get_user_model()

Priority = (
    ('H', 'High'),
    ('Medium', 'Medium'),
    ('L', 'Low')
)


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    creator = models.CharField(max_length=20)
    noOfTeamMembers = models.IntegerField()
    priority = models.CharField(max_length=6, choices=Priority)
    typeOfProject = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    pass


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    designation = models.CharField(max_length=32)
    pass


Status = (
    ('O', 'Open'),
    ('I', 'InProgress'),
    ('C', 'Closed')
)
Type = (
    ('S', 'Story'),
    ('T', 'Task'),
    ('B', 'Bug')
)


class Issue(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=32)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=Type)
    status = models.CharField(max_length=7, choices=Status)
    label = models.CharField(max_length=10)
    priority = models.CharField(max_length=6, choices=Priority)
    start_date = models.DateField()
    end_date = models.DateField()

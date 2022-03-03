from rest_framework import serializers

from .models import Person, Project, User, Issue


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'creator', 'noOfTeamMembers', 'priority', 'typeOfProject', 'start_date',
                  'end_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        field = ['id', 'name', 'designation']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        field = ['id', 'project', 'description', 'assigned_to', 'priority', 'start_date', 'end_date']


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
        permissions = [
            ("add_project", "Can add the projects"),
            ("change_project_priority", "Can change the priority of projects"),
            ("view_project", "Can view the projects"),
            ("delete_project", "Can delete the projects"),
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        field = ['id', 'name', 'designation']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        field = ['id', 'project', 'title', 'description', 'assigned_to', 'type', 'status', 'label', 'priority',
                 'start_date', 'end_date']
        permissions =[
            ("add_issue", "Can add the issues"),
            ("view_issue", "Can view the issues"),
            ("change_issue_status", "Can change the status of issues"),
            ("delete_issue", "Can delete the issues")
        ]


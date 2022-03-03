from django.apps import AppConfig


class PersonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persons'


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects'


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


class IssuesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'issues'

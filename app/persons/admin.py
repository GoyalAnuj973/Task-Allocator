from django.contrib import admin

from .models import Person, Project, Issue, User

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Issue)


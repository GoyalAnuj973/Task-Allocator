from xml.etree.ElementInclude import include

from django.urls import path

# from . import admin
from .views import PersonView, ProjectView, IssueView, UserView
from rest_framework import routers

# from .. import persons

# router = routers.DefaultRouter()
# router.register(r'persons', PersonView, basename='Person')
# router.register(r'projects', ProjectView, basename='Project')
# router.register(r'users', UserView, basename='User')
# router.register(r'issues', IssueView, basename='Issue')

urlpatterns = [
    path("", PersonView.as_view()),
    path("projects", ProjectView.as_view()),
    path("users", UserView.as_view()),
    path("issues", IssueView.as_view()),
    # path('', include(router.urls)),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/persons/', include(persons.urls)),
#     path('api/projects/', include('projects.urls')),
#     path('api/issues/', include('issues.urls')),
#     path('api/users/', include('users.urls'))
# ]
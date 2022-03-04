from xml.etree.ElementInclude import include

from django.urls import path

# from . import admin
from .views import PersonView, ProjectView, IssueView, UserView, IssueProjectView
from rest_framework.authtoken import views
from rest_framework import routers

# from .. import persons

# router = routers.DefaultRouter()
# router.register(r'persons', PersonView, basename='Person')
# router.register(r'projects', ProjectView, basename='Project')
# router.register(r'users', UserView, basename='User')
# router.register(r'issues', IssueView, basename='Issue')

urlpatterns = [
    path("", PersonView.as_view()),

    # Token Authentication
    path('api-token-auth/', views.obtain_auth_token),

    # path('register', views.RegisterUser.as_view()),

    # all projects
    path("projects", ProjectView.as_view()),

    # project by id (pk -> project_id)
    path("projects/<int:pk>", ProjectView.as_view()),

    # Users
    path("users", UserView.as_view()),

    # Issues
    path("issues", IssueView.as_view()),

    # issues of a project
    path("issues/project/<int:project>", IssueView.as_view()),

    # all issues of a project id
    path("issues/assigned_to/<int:assigned_to>", IssueView.as_view()),

    # show all issues of a project with pagination
    path("issues/project/pagination/<int:project>", IssueProjectView.as_view())

    # path('', include(router.urls)),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/persons/', include(persons.urls)),
#     path('api/projects/', include('projects.urls')),
#     path('api/issues/', include('issues.urls')),
#     path('api/users/', include('users.urls'))
# ]

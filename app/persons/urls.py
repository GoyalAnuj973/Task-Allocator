from django.urls import path

from .views import PersonView, ProjectView, IssueView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', ProjectView, basename='Project')

urlpatterns = [
    path("", PersonView.as_view()),
    path("", ProjectView.as_view()),
    path("", IssueView.as_view()),
]

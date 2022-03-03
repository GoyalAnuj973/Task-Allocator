from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person, Issue, User
from .serializers import PersonSerializer, IssueSerializer, UserSerializer

from .models import Project
from .serializers import ProjectSerializer


class PersonView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        response = PersonSerializer(persons, many=True)
        return Response({"data": response.data})

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ProjectView(APIView):
    def get(self, request, pk=None, format=None):
        # projects = Project.objects.all()
        # response = ProjectSerializer(projects, many=True)
        if pk is not None:
            project = self.objects.get(pk=pk)
            response = ProjectSerializer(project)
        # if(Project.id) return Response({"data":})
        else:
            project = Project.objects.all()
            response = ProjectSerializer(project, many=True)

        return Response({"data": response.data})

    # def get_project_by_id(self, request, project_id):
    #     try:
    #         project = Project.objects.get(project_id=project_id)
    #     except Project.DoesNotExist:
    #         raise Http404
    #     project.delete()
    #     return Response(status=status.HTTP_)

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        response = ProjectSerializer(users, many=True)
        return Response({"data": response.data})

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class IssueView(APIView):
    def get(self, request):
        issues = Issue.objects.all()
        response = ProjectSerializer(issues, many=True)
        return Response({"data": response.data})

    def post(self, request):
        data = request.data
        serializer = IssueSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

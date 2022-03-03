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
    def get(self, request):
        projects = Project.objects.all()
        response = ProjectSerializer(projects, many=True)
        # if(Project.id) return Response({"data":})
        return Response({"data": response.data})

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



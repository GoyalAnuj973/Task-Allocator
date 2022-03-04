from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .models import Person, Issue, User
from .serializers import PersonSerializer, IssueSerializer, UserSerializer

from .models import Project
from .serializers import ProjectSerializer


# View class for persons
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


# View class for projects
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


# View class for users
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        response = UserSerializer(users, many=True)
        return Response({"data": response.data})

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


# View class for issues
class IssueView(APIView):
    # def get(self, request, project, pk=None):
    #
    #     # issues = Issue.objects.all()
    #     # response = IssueSerializer(issues, many=True)
    #     # return Response({"data": response.data})
    #     if pk is not None:
    #         try:
    #             issue = Issue.objects.get(pk=project)
    #         except Issue.DoesNotExist:
    #             raise Http404
    #         serializer = serializers.IssueSerializer(issue)
    #         return Response(serializer.data)
    #     # return Response({"data": })

    # getting the issues data
    def get(self, request, project=None, assigned_to=None):
        if project is not None:
            issues = Issue.objects.filter(project=project)

        elif assigned_to is not None:
            issues = Issue.objects.filter(assigned_to=assigned_to)

        else:
            issues = Issue.objects.all()

        response = IssueSerializer(issues, many=True)
        return Response(response.data)

    def post(self, request):
        data = request.data
        serializer = IssueSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request):
        id = request.query_params("id")
        if id is not None:
            try:
                issue = Issue.objects.get(id=id)
            except Exception as e:
                print(e)
                return Response({'message': 'The issue does not exist'}, status=404)

        data = request.GET.get('assigned_to')
        print(data)
        user = User.objects.get(id=data)
        print(user)
        issue.assigned_to = user
        issue.save()
        serializer = IssueSerializer(issue)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        return Response(serializer.data, status=201)

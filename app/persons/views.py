from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.templatetags.rest_framework import data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token

from . import serializers
from .models import Person, Issue, User
from .serializers import PersonSerializer, IssueSerializer, UserSerializer

from .models import Project
from .serializers import ProjectSerializer


# Authentication class
# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UsersSerializer(data=request.data)
#
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
#
#         serializer.save()
#         user = User.objecs.get(username=serializer.data['username'])
#         token_obj, _ = Token.objects.get_or_create(user=user)
#         return Response(
#             {'status': 200, 'payload': serializer.data, 'token': str(token_obj), 'message': 'your data is saved'})


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
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def get(self, request, project, pk=None):
        # issues = Issue.objects.all()
        # response = IssueSerializer(issues, many=True)
        serializer = PersonSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


# View class for projects
class ProjectView(APIView):
    permission_classes = (IsAuthenticated,)

    # serializer = UserSerializer(data=data)
    # serializer.is_valid(raise_exception=True)
    # serializer.save()
    # return Response(serializer.data, status=201)

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


# Pagination for Issues of Project

class IssueProjectView(APIView):

    @api_view(['GET', ])
    @permission_classes([AllowAny, ])
    def get(self, request, project=None):
        if project is not None:
            issues = Issue.objects.filter(project=project)

        else:
            issues = Issue.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = 50
        issues_objects = Issue.objects.all()
        result_page = paginator.paginate_queryset(issues_objects, request)
        serializer = IssueSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

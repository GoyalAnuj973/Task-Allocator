from django.test import TestCase

from .models import *
from rest_framework.test import APITestCase


# Unit Test for Persons
class TestPersons(APITestCase):

    def setUp(self):
        # create test data
        self.person_1 = Person.objects.create(name="Rhea", age=24)
        self.person_2 = Person.objects.create(name="Aman", age=24)

    def test_get_people(self):
        response = self.client.get('/api/persons/')
        self.assertEqual(response.status_code, 200)
        # the size should be 2
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 2)

    def test_create_new_person(self):
        response = self.client.post('/api/persons/', {'name': 'User1', 'age': 25})
        # the new person should be created
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        # verify that the details are correct
        self.assertEqual(response_data.get('name'), 'User1')
        self.assertEqual(response_data.get('age'), 25)

        # now the get api should return 3 people
        response = self.client.get('/api/persons/')
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 3)

        # More examples can be found here: https://www.django-rest-framework.org/api-guide/testing/#example


# Unit Test for Projects
class TestProjects(APITestCase):

    def setUp(self):
        # create test data
        self.project_1 = Project.objects.create(name="Java Project", description="this is a project", creator="Anuj",
                                                noOfTeamMembers="3", priority="High", typeOfProject="Technology",
                                                start_date="2022-03-03", end_date="2022-03-05")
        self.project_2 = Project.objects.create(name="Python Project", description="this is a project",
                                                creator="Anaya", noOfTeamMembers="5", priority="Medium",
                                                typeOfProject="Technology", start_date="2022-03-05",
                                                end_date="2022-03-05")

    def test_get_project(self):
        response = self.client.get('/api/persons/projects/')
        self.assertEqual(response.status_code, 200)
        # the size should be 2
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 2)

    def test_create_new_project(self):
        response = self.client.post('/api/persons/projects/',
                                    {'name': "Angular Project", 'description': " this project",
                                     'creator': "someone", 'noOfTeamMembers': 2, 'priority': "Low",
                                     'typeOfProject': 'Tech', 'start_date': "2022-03-03",
                                     'end_date': '2022-03-05'})
        # the new project should be created
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        # verify that the details are correct
        self.assertEqual(response_data.get('name'), 'Angular Project')
        self.assertEqual(response_data.get('noOfTeamMembers'), 2)

        # now the get api should return 3 people
        response = self.client.get('/api/persons/projects/')
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 3)


# Unit Test for Issues
class TestIssues(APITestCase):
    def setUp(self):
        # create test data
        self.person_1 = Project.objects.create(project="Java", description="This project", assigned_to="anuj",
                                               type="Task", status="Open", label="navbar", priority="High",
                                               start_date="2022-03-03", end_date="2022-03-05")
        self.person_2 = Project.objects.create(project="Python", description="This project", assigned_to="user2",
                                               type="Task", status="Closed", label="navbar", priority="Medium",
                                               start_date="2022-03-03", end_date="2022-03-05")

    def test_get_issue(self):
        response = self.client.get('/api/persons/issues/')
        self.assertEqual(response.status_code, 200)
        # the size should be 2
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 2)

    def test_create_new_issue(self):
        response = self.client.post('/api/persons/issues/', {'project': 'angular', 'description': "This project",
                                                             'assigned_to': "user3", 'type': "Task", 'status': "Open",
                                                             'label': "navbar", 'priority': "High",
                                                             'start_date': "2022-03-03",
                                                             'end_date': "02022-03-05"})
        # the new project should be created
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        # verify that the details are correct
        self.assertEqual(response_data.get('project'), 'angular')
        self.assertEqual(response_data.get('description'), 'This project')

        # now the get api should return 3 people
        response = self.client.get('/api/persons/issues/')
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 3)


# Unit Test for Users
class TestUsers(APITestCase):
    def setUp(self):
        # create test data
        self.person_1 = Project.objects.create(name="Rhea", designation="developer")
        self.person_2 = Project.objects.create(name="Aman", designation="Tester")

    def test_get_users(self):
        response = self.client.get('/api/persons/users/')
        self.assertEqual(response.status_code, 200)
        # the size should be 2
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 2)

    def test_create_new_user(self):
        response = self.client.post('/api/persons/users/', {'name': 'User1', 'designation': 'Tester'})
        # the new project should be created
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        # verify that the details are correct
        self.assertEqual(response_data.get('name'), 'User1')
        self.assertEqual(response_data.get('designation'), 'Tester')

        # now the get api should return 3 people
        response = self.client.get('/api/persons/users/')
        response_data = response.json()
        self.assertEqual(len(response_data.get('data')), 3)

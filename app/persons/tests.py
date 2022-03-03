from django.test import TestCase

from .models import *
from rest_framework.test import APITestCase

class TestPersons(APITestCase):

  def setUp(self):

    #create test data
    self.person_1 = Person.objects.create(name="Rhea", age=24)
    self.person_2 = Person.objects.create(name="Aman", age=24)

  def test_get_people(self):

    response = self.client.get('/api/persons/')
    self.assertEqual(response.status_code, 200)
    #the size should be 2
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),2)

  def test_create_new_person(self):
    response = self.client.post('/api/persons/', {'name': 'User1', 'age': 25})
    #the new person should be created
    self.assertEqual(response.status_code, 201)
    response_data = response.json()
    #verify that the details are correct
    self.assertEqual(response_data.get('name'), 'User1')
    self.assertEqual(response_data.get('age'), 25)

    #now the get api should return 3 people
    response = self.client.get('/api/persons/')
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),3)

    #More examples can be found here: https://www.django-rest-framework.org/api-guide/testing/#example


class TestProjects(APITestCase):

  def setUp(self):

    #create test data
    self.person_1 = Project.objects.create(name="Rhea", age=24)
    self.person_2 = Project.objects.create(name="Aman", age=24)

  def test_get_project(self):

    response = self.client.get('/api/projects/')
    self.assertEqual(response.status_code, 200)
    #the size should be 2
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),2)

  def test_create_new_project(self):
    response = self.client.post('/api/projects/', {'name': 'User1', 'age': 25})
    #the new project should be created
    self.assertEqual(response.status_code, 201)
    response_data = response.json()
    #verify that the details are correct
    self.assertEqual(response_data.get('name'), 'User1')
    self.assertEqual(response_data.get('age'), 25)

    #now the get api should return 3 people
    response = self.client.get('/api/projects/')
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),3)

class TestIssues(APITestCase):
  def setUp(self):

    #create test data
    self.person_1 = Project.objects.create(name="Rhea", age=24)
    self.person_2 = Project.objects.create(name="Aman", age=24)

  def test_get_issue(self):

    response = self.client.get('/api/projects/')
    self.assertEqual(response.status_code, 200)
    #the size should be 2
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),2)

  def test_create_new_issue(self):
    response = self.client.post('/api/projects/', {'name': 'User1', 'age': 25})
    #the new project should be created
    self.assertEqual(response.status_code, 201)
    response_data = response.json()
    #verify that the details are correct
    self.assertEqual(response_data.get('name'), 'User1')
    self.assertEqual(response_data.get('age'), 25)

    #now the get api should return 3 people
    response = self.client.get('/api/projects/')
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),3)

class TestUsers(APITestCase):
  def setUp(self):

    #create test data
    self.person_1 = Project.objects.create(name="Rhea", age=24)
    self.person_2 = Project.objects.create(name="Aman", age=24)

  def test_get_users(self):

    response = self.client.get('/api/projects/')
    self.assertEqual(response.status_code, 200)
    #the size should be 2
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),2)

  def test_create_new_user(self):
    response = self.client.post('/api/projects/', {'name': 'User1', 'age': 25})
    #the new project should be created
    self.assertEqual(response.status_code, 201)
    response_data = response.json()
    #verify that the details are correct
    self.assertEqual(response_data.get('name'), 'User1')
    self.assertEqual(response_data.get('age'), 25)

    #now the get api should return 3 people
    response = self.client.get('/api/projects/')
    response_data = response.json()
    self.assertEqual(len(response_data.get('data')),3)





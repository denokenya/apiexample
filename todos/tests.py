from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo')
        Todo.objects.create(description='a description here')

    def test_title_content(self):
        todo = Todo.objects.get(id=12)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_description_content(self):
        todo = Todo.objects.get(id=20)
        expected_object_name = f'{todo.description}'
        self.assertEquals(expected_object_name, 'a description here')
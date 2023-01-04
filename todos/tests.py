from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Learn python",
            body="A body text here"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Learn python")
        self.assertEqual(self.todo.body, "A body text here")
        self.assertEqual(str(self.todo), "Learn python")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={
                "pk": self.todo.id
            }),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Learn python")

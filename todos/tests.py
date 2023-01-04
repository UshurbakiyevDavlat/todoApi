from django.test import TestCase

# Create your tests here.

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

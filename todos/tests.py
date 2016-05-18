from django.test import TestCase
from todos.models import TodoItem

class TodoTests(TestCase):
	"""TodoItem model tests."""
	def test_str(self):
		todo = TodoItem(text='This is something to be done!  ')
		self.assertEquals(str(todo),'This is something to be done!  ')


from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TodoItem(models.Model):
	owner = models.ForeignKey(User)
	text = models.CharField(max_length=100)
	def __str__(self):
		return self.text
	def get_absolute_url(self):
		return reverse('item-view', kwargs={'pk': self.id})
	
	due_date = models.DateField(null=True,blank=True)
	todo_date = models.DateField(null=True,blank=True)
	start_time = models.DateField(null=True,blank=True)
	end_time = models.DateField(null=True,blank=True)

	completed = models.BooleanField(default=False)

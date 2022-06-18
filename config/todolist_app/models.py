from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoTask(models.Model):
	todoName = models.CharField(max_length=50)
	content  = models.CharField(max_length=250)
	created_date = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.todoName}'

	class Meta:
		ordering = ['-created_date']

	

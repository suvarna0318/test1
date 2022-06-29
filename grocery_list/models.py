from django.db import models
from django.utils import timezone

class Products(models.Model):
	title=models.CharField(max_length=200)
	qty=models.CharField(max_length=100)
	date_posted=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

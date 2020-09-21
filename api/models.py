from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=60)
	image = models.ImageField(upload_to='pictures/')

	def __str__(self):
		return self.title

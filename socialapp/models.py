from django.db import models

# Create your models here.
class SocialApp(models.Model):
	title = models.CharField(max_length = 200)
	name = models.CharField(max_length = 100)
	contact = models.CharField(max_length = 10)

	def __str__(self):
		return self.name

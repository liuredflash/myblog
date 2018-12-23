from django.db import models

class Post(models.Model):
	uid = models.IntegerField()
	title = models.CharField(max_length=64)
	create = models.DateTimeField(auto_now_add=True)
	content = models.TextField()


class Comment(models.Model):
	pid = models.IntegerField()
	uid = models.IntegerField()
	create = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
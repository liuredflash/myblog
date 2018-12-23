from django.db import models

class User(models.Model):
	SEX = (
	       ("F", "女"),
	       ("M", "男"),
	       ("U", "保密")
	)
	user_name = models.CharField(max_length=32, unique=True)
	password = models.CharField(max_length=128)
	age = models.IntegerField()
	sex = models.CharField(choices=SEX, max_length=8)
	icon = models.ImageField()

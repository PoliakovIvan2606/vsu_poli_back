from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=120)
    age = models.IntegerField()
    height = models.IntegerField()
    email = models.EmailField()

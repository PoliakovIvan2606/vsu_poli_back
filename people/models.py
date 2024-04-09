from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=120)
    age = models.IntegerField()
    height = models.IntegerField()
    email = models.EmailField()

class News(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='', null=True)

    def __str__(self):
        return self.title

class Departments(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()
    image = models.ImageField(upload_to='', null=True)
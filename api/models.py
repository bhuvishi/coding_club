from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    grade = models.IntegerField()
    stage = models.IntegerField()

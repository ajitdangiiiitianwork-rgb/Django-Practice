from django.db import models

# Create your models here.
class Student(models.Model):
  name    =     models.CharField(max_length=20)
  age     =     models.IntegerField()
  email   =     models.EmailField()
  address =     models.TextField()


class Car(models.Model):
  c_name  =     models.CharField(max_length = 20)
  speed   =     models.IntegerField(default=50)

  def __str__(self):
    return self.c_name
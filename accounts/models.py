from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=100, unique=True)
  profile_image = models.ImageField()
  user_bio = models.CharField(max_length=50)

  USERNAME_FIELD =  'phone_number'
  REQUIRED_FIELDS = []
  objects = UserManager()

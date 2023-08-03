from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=255, default=None, unique=True)
    is_superuser = models.BooleanField(default=False)
    

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields here if needed
    pass


from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=250)
    GAcohort = models.CharField(max_length=50, blank=True)
    LinkedIn = models.CharField(max_length=250, blank=True)
    GitHub = models.CharField(max_length=250, blank=True)
    Instagram = models.CharField(max_length=250, blank=True)
    Twitter = models.CharField(max_length=250, blank=True)
    personal_site= models.CharField(max_length=250, blank=True)


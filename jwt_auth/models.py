from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=250, default='https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png')
    GAcohort = models.CharField(max_length=50, blank=True)
    LinkedIn = models.CharField(max_length=250, blank=True)
    GitHub = models.CharField(max_length=250, blank=True)
    Instagram = models.CharField(max_length=250, blank=True)
    Twitter = models.CharField(max_length=250, blank=True)
    personal_site= models.CharField(max_length=250, blank=True)
    created_project = models.CharField(max_length= 250, blank=True)


from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    image_profile = models.ImageField(null=True,blank=True,upload_to="profiles/")
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.username


from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    price = models.FloatField(null=True,blank=True,)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
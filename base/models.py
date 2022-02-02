from django.db import models

# Create your models here.

class Pet(models.Model):
    type = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pet(models.Model):
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)

    owner = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.body[0:50])

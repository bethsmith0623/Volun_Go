from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.ManyToManyField(Event)

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenum = models.CharField(max_length=100)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# migrations for user model already made




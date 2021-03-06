from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Events attending

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attending = models.ManyToManyField(User, related_name='attendee')

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phonenum = models.CharField(max_length=100)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# migrations for user model already made




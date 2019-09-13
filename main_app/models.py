from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    orghost = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    def __str__(self):
        return self.title

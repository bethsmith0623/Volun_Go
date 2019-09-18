from django.forms import ModelForm
from .models import Event

class EventAttendForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title','date','location']
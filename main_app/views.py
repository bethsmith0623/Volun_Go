from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Event, Organization, User
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import EventAttendForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def account_detail(request):
    events = Event.objects.filter(user=request.user)
    event_attend = User.objects.get(id=request.user.id).attendee.all()
    return render (request, 'accounts.html',{'event_attend': event_attend, 'events': events}) 
    
def event_attend(request, event_id):
    Event.objects.get(id=event_id).attending.add(request.user)
    return redirect('accounts')

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', { 'event': event })

def orgs_index(request):
   orgs = Organization.objects.all()
   return render(request, 'main_app/orgs_index.html', {'orgs': orgs})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class EventCreate(CreateView):
    model = Event
    fields = ['title','description','location','date','duration']
    success_url = '/events/'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventUpdate(UpdateView):
    model = Event
    fields = ['description','location','date','duration']

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'

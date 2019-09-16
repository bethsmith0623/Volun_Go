from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Event, Organization
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')







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
        return render(request, 'registration/singup.html', context)




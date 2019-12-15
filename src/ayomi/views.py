# coding: utf-8

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from ayomi.forms import SignUpForm
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'home.html', {'form': form})

@login_required
def profile (request):
    return render (request, 'profile.html')
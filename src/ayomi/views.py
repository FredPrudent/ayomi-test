# coding: utf-8

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm
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
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render (request, 'profile.html', {'form': form})


    else:
        form= UserUpdateForm(instance=request.user)
    return render (request, 'profile.html', {'form': form})
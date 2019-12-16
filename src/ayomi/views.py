# coding: utf-8

from django.contrib.auth import login, authenticate, logout as user_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, LoginForm
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
def logout(request):
    user_logout(request)
    return redirect ('home')

@login_required
def account_redirect(request):
    return redirect('account-landing', pk=request.user.pk, name=request.user.email)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            
            user = authenticate()
            
            
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

        
    

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
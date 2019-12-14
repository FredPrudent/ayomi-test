# coding: utf-8
# from django.shortcuts import render
# from .forms import SignUpForm

# def home (request):
#     title = "Bienvenue"
    
#     form = SignUpForm(request.POST or None)

#     if request.user.is_authenticated():
#         title = "Bienvenue %s" %(request.user)

#     context = {
#         "title": title,
#         "form" : form
#     }

    

#     if form.is_valid():
#         instance = form.save (commit=False)
#         instance.save()
#         context = {
#             "title" : "Vous vous êtes bien enregistré"
#         }

    
#     return render(request, "base.html", context)

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'home.html', {'form': form})


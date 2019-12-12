# coding: utf-8
from django.shortcuts import render
from .forms import SignUpForm

def home (request):
    title = "Bienvenue"
    
    form = SignUpForm(request.POST or None)

    if request.user.is_authenticated():
        title = "Bienvenue %s" %(request.user)

    context = {
        "title": title,
        "form" : form
    }

    

    if form.is_valid():
        instance = form.save (commit=False)
        instance.save()
        context = {
            "title" : "Vous vous êtes bien enregistré"
        }

    
    return render(request, "home.html", context)


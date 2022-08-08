from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
def home(reguest):
    projects = Project.objects.all()
    return render(reguest, 'portfolio/home.html', {'projects': projects})
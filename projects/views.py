from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.


def all_projects(request):
    # query database to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})

from django.shortcuts import render
from django.http import HttpResponse

from section.models import Project

def homePage(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'project': projects})

# Create your views here.

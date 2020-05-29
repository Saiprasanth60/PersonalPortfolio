from django.shortcuts import render
from .models import project

# Create your views here.

def home(request):
    project_data = project.objects.all()
    return render(request, "home.html", {'data':project_data})
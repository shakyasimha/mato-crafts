from django.shortcuts import render
from django.http import HttpResponse 

from .models import person_collection 

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome.</h1>")
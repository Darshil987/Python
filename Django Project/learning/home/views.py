from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hview(req):
    return HttpResponse('<h1>Hello! Welcome, This is First Page</h1><p>Welcome, Good Morning</p>')

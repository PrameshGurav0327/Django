from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def superman(request):
    return HttpResponse("<h1>I am superman</h1>")

def batman(request):
    return HttpResponse("<h1>I am batman</h1>")

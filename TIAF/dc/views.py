from django.shortcuts import render

def index(request):
    return render(request, 'dc/index.html')

def superman(request):
    return render(request, 'dc/superman.html')
from django.shortcuts import render
from .models import marvelModel
# Create your views here.
def index(request):
    mf = marvelModel.objects.all()
    return render(request, 'core/index.html', {"mf":mf})

from django.shortcuts import render,redirect
from .models import MarvelModel
from .forms import MarvelForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        mf = MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/')
    else:
        mf=MarvelForm()
        mm=MarvelModel.objects.all()
    return render(request,'core/index.html',{"mm":mm,'mf':mf})


def delete_avenger(request,id):
    mm = MarvelModel.objects.get(pk=id)
    mm.delete()
    return redirect("/")

from django.shortcuts import render, redirect, get_object_or_404
from .models import MarvelModel
from .forms import MarvelForm

def update_avenger(request, id):
    mm = get_object_or_404(MarvelModel, pk=id)  # Ensures object exists

    if request.method == "POST":
        mf = MarvelForm(request.POST, instance=mm)  # Correcting variable name
        if mf.is_valid():
            mf.save()
            return redirect("/")  # Redirect after successful update
    else:
        mf = MarvelForm(instance=mm)  # Initialize form for GET request
    
    return render(request, "core/update.html", {"mf": mf})  # Ensure response is always returned

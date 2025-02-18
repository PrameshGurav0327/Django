from django.shortcuts import render

# Create your views here.
def index(request):
    # context={"villain":"zola"}
    return render(request, 'core/index.html',{'villain':'redskull'})


def hero(request):
    return render(request,'core/hero.html',{"hero":["captain america","ironman","spiderman","thor","black panther","black widow","hulk"]})



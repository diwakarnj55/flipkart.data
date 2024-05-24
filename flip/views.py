from django.shortcuts import render
from . models import advertisement

def index(request):
    item=advertisement.objects.all()
    return render(request,"index.html",{"item":item})

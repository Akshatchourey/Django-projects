from django.shortcuts import render
from .models import Store

# Create your views here.


def index(request):
    stor = Store.objects.all()
    return render(request, "datatoviwe/index.html", {'sho': stor})


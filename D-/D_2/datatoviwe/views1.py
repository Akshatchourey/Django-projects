from django.shortcuts import render

# Create your views hare.


def login(request):
    return render(request, "datatoviwe/login.html")

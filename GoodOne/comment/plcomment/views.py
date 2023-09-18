from django.shortcuts import render
from django.http import HttpRequest
from .models import Profile
# id--->Akshat_C, pass-->12345

def index(request):
    return render(request, 'plcomment/index.html',{'message':' '})

def saveProfile(request):
    message = " "
    if request.method == "POST":
        firstname = request.POST.get('firstName')  # name in html
        lastname = request.POST.get('lastName')
        username = request.POST.get('userName')
        state = request.POST.get('state')
        city = request.POST.get('city')
        number = request.POST.get('phoneNo')
        terms = request.POST.get("termsAnsConditions", "off")
        if terms == "on":
            my_data = Profile(firstName=firstname, lastname=lastname, username=username, state=state, city=city, phoneNo=number)
            my_data.save()
            message = "data saved"

    return render(request, 'plcomment/index.html',{'message':message})

def show(request):
    profiles = Profile.objects.all()
    return render(request, 'plcomment/show.html', {'profile': profiles})

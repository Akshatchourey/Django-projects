from django.shortcuts import render
from .forms import Studentregister

# Create your views here.

# auto_id=True,label_suffix=' ',
def index(request):
    forme = Studentregister(initial={'name': "Akshat"})
    return render(request, 'API/index.html', {'for': forme})


def done(request):
    p = request.GET.get('password', '12345')
    if len(p) <= 8:
        go = {'what': 'Not Done', }
        return render(request, 'API/done.html', go)
    else:
        go = {'what': 'Done', }
        return render(request, 'API/done.html', go)
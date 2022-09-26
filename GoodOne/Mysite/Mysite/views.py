from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {"name":'akshat',"place":'mars'}
    return render(request, "index.html",params)
   # return HttpResponse("Hallow World")


def youtube(request):
    return HttpResponse('''<a href="https://www.youtube.com/channel/UC4K_EvtcYbLX59lqH2ZbQ3A/featured">uk</a>''')


def analyze(request):
    Djtext = request.GET.get("text","default")
    removepunc = request.GET.get("removepunc","off")
    capitalizefirst = request.GET.get("capitalizefirst","off")
    newlineremover = request.GET.get("newlineremover","off")
    spaceremover = request.GET.get("spaceremover","off")
    charcount = request.GET.get("charcount","off")
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = Djtext
    while removepunc == 'on':
        analyzed = ""
        for i in Djtext:
            if i not in punc :
                analyzed = analyzed + i
        removepunc = 'off'
    while capitalizefirst == 'on':
        analyzed = analyzed.capitalize()
        capitalizefirst = 'off'
    while spaceremover == 'on':
        u=""
        for i in analyzed:
            if i is not " ":
               u = u + i
        analyzed = u
        spaceremover = 'off'
    while charcount == 'on':
        analyzed = len(analyzed)
        charcount = 'off'
    params = {"analyzed_text": analyzed}
    return render(request,"analyze.html", params)


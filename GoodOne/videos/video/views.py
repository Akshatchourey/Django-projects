from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from math import ceil as c


def index(request):
    return render(request, "video/index.html")
def video(request):
    no_of_videos = 12
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    videos = Video.objects.all()
    length = len(videos)
    videos = videos[(page-1)*no_of_videos: page*no_of_videos]
    if page>1:
        prev=page-1
    else:
        prev = None
    if page < c(length/no_of_videos):
        nxt = page + 1
    else:
        nxt = None
    context = {'videos': videos, 'prev': prev, 'nxt': nxt}
    return render(request, "video/videos.html", context)

def video_playing(request, slug):
    videoFound = Video.objects.filter(slug=slug).first()
    context = {'name': videoFound, 'types':videoFound.source[0:5]}
    return render(request, "video/video_playing.html", context)

def playlist(request):
    playlists = Playlist.objects.all()
    return render(request, "video/playlist.html", {'playlists':playlists})

def plvideos(request, slug):
    videos = Video.objects.filter(slug__regex=f"^{slug}.*")
    return render(request, "video/videos.html", {'videos':videos})      

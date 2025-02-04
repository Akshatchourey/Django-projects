from django.urls import path
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
# For views
    path('', views.index, name='home'),
    path('videos/', views.video, name='video'),
    path('video_playing/<str:slug>', views.video_playing, name='video_playing'),
    path('playlists/', views.playlist, name='playlist'),
    path('playlist/<str:slug>', views.plvideos, name='vodeo_in_playlist')

]

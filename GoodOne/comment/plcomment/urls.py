from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="showIndexPage"),
    path('saveProfile', views.saveProfile, name="saveMyProfile"),
    path('show/', views.show, name="show"),
]

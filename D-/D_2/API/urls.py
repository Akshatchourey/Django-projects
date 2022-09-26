from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="forms"),
    path('done/', views.done, name="done"),
]
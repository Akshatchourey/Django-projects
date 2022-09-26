from django.urls import path
from .import views
from .import views1

urlpatterns = [
    path('', views.index, name='table'),
    path('login', views1.login, name='login'),
]

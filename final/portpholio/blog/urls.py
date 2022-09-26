from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('edu/', views.edu, name='edu'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('blogpost_edu/<str:slug>', views.blogpost_edu, name='blogpost_edu'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]

from django.urls import path
from .import views

urlpatterns = [
    # REST-APIs
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),
]

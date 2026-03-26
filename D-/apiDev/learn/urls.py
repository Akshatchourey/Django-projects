from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('students', views.studentView, name="StudentsView"),
    path('student/<int:pk>/', views.studentDetailView),
]

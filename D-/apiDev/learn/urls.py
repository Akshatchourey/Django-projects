from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees_view_set', views.EmployeeViewSet, basename="employees_view_set")
router.register('employees_Model_view_set', views.EmployeeModelViewSet)

urlpatterns = [
    path('', views.home, name="home"),

    # REST-APIs
    path('students', views.studentView, name="StudentsView"),
    path('student/<int:pk>/', views.studentDetailView),
    path('employees/', views.Employees.as_view(), name="AllEmployees"),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('employees_mixins/', views.EmployeesMixins.as_view()),
    path('employees_generics/<int:pk>/', views.EmployeesGenerics.as_view()),

    path('', include(router.urls)),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/employees/', views.EmployeesView.as_view()),
    path('api/employers/', views.EmployersView.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('incidents/', views.incidents, name='incidents'),
    path('incidents/details/<int:id>', views.details, name='details'),
    path('details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),    
]
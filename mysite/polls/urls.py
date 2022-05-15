from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.get_name, name='landing'),
]
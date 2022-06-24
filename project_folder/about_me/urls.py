from django.urls import path
from about_me import views

urlspatterns = [
    path('', views.index, name='index'),
]
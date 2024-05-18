from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('places/', views.PlaceList, name='placeList'),
    path('placescreate/', views.PlaceCreate, name='placeCreate'),
]
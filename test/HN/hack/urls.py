from django.urls import path
from . import views

#urls goes here

urlpatterns = [
    path('', views.index, name='home'),
]

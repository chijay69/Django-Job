from . import views
from django.urls import path

#urls goes here

urlpatterns = [
    path('', views.index, name = 'index'),
]

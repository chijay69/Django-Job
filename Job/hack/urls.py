from django.urls import path
from . import views

#urls goes here

urlpatterns = [
    #path('', views.index, name='home'),
    path('', views.post_list, name='post_list'),
    path('<int:id>/',
         views.post_detail,
         name='post_detail'),
    path('search/', views.post_search, name='post_search'),
]

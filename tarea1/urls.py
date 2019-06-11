from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('films/<str:id>/', views.movie, name='movie'),
    path('people/<str:id>/', views.people, name='people'),
    path('planets/<str:id>/', views.planet, name='planet'),
    path('starships/<str:id>/', views.starship, name='starship'),
    ]

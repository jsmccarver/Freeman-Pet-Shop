from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/<str:pk>', views.pets, name='room')
]
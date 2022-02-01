from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<str:pk>', views.pet, name='pet')
]
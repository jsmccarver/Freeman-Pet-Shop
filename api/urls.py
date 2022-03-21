from django.urls import path
from . import views
urlpatterns = [
    path('', views.getPet),
    path('add', views.addPet),
]

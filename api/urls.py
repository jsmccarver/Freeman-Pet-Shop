from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('/pet', views.getPets),
    path('/pet/:id', views.getPets),
    path('add', views.addPet),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('pets', views.getPets),
    path('add', views.addPet),
]

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<str:pk>', views.pet, name='pet'),
    path('create-pet', views.create_pet, name='create-pet'),
]

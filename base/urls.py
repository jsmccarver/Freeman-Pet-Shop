from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),


    path('pet/<str:pk>', views.pet, name='pet'),
    path('create-pet/', views.create_pet, name='create-pet'),
    path('update-pet/<str:pk>/', views.update_pet, name='update-pet'),
    path('delete-pet/<str:pk>', views.delete_pet, name='delete-pet'),


    path('room/<str:pk>', views.room, name='room')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

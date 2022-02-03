from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<str:pk>', views.pet, name='pet'),
    path('create-pet', views.create_pet, name='create-pet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

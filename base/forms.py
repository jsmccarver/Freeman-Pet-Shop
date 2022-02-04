from django.forms import ModelForm
from .models import Pet, Room


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

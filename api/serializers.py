from rest_framework import  serializers
from base.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
            model = Pet
            fields = '__all__'
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Pet
from .serializers import PetSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/Pet',
        'GET /api/Pet/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getPets(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPet(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addPet(request):
    serializer = PetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

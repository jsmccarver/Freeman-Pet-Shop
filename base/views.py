from django.shortcuts import render
from .models import Pet
# Create your views here.
#pets = [
#        {'id': 1, 'name': 'Lets learn python!'},
#        {'id': 2, 'name': 'Design with me'},
#        {'id': 3, 'name': 'Frontend developers'},
#    ]
pets = Pet.objects.all()

def home(request):
    context = {'pets' : pets}
    return render(request, 'base/home.html', context)
    
def pet(request, pk):
    pet = Pet.objects.get(id=pk)
    context = {'pet' : pet}
    return render(request, "base/pets.html", context)
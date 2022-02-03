from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm
# Create your views here.
# pets = [
#        {'id': 1, 'name': 'Lets learn python!'},
#        {'id': 2, 'name': 'Design with me'},
#        {'id': 3, 'name': 'Frontend developers'},
#    ]


def home(request):
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'base/home.html', context)


def pet(request, pk):
    pet = Pet.objects.get(id=pk)
    context = {'pet': pet}
    return render(request, "base/pets.html", context)


def create_pet(request):
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/pets_form.html', context)


def updateRoom(request, pk):
    pet = Pet.objects.get(id=pk)
    form = PetForm(instance=pet)
    context = {'form'}
    return render(request, 'base/pet_form.html', context)

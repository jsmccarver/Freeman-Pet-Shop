from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Pet, Room, Type
from .forms import PetForm


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Does Not Exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured during registration')
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    pets = Pet.objects.filter(Q(type__name__icontains=q) |
                              Q(name__icontains=q) |
                              Q(breed__icontains=q)
                              )
    rooms = Room.objects.all()
    types = Type.objects.all()
    pet_count = pets.count()
    context = {'pets': pets,
               'rooms': rooms,
               'types': types,
               'pet_count': pet_count,
               }
    return render(request, 'base/home.html', context)


def pet(request, pk):
    pet = Pet.objects.get(id=pk)
    context = {'pet': pet}
    return render(request, "base/pets.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def create_pet(request):
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/pets_form.html', context)


@login_required(login_url='login')
def update_pet(request, pk):
    pet = Pet.objects.get(id=pk)
    form = PetForm(instance=pet)
    if request.user != pet.poster:
        return HttpResponse('You can not update pets you do not own')
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/pets_form.html', context)


@login_required(login_url='login')
def delete_pet(request, pk):
    pet = Pet.objects.get(id=pk)
    if request.user != pet.poster:
        return HttpResponse('You can not update pets you do not own')
    if request.method == 'POST':
        pet.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': pet})

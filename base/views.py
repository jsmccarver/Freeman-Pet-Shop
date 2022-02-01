from django.shortcuts import render
# Create your views here.

def home(request):
    rooms = [
        {'id': 1, 'name': 'Lets learn python!'},
        {'id': 2, 'name': 'Design with me'},
        {'id': 3, 'name': 'Frontend developers'},
    ]
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context)
    
def pets(request, pk):
    context = {
        "first_name" : "Naveen",
        "last_name"  : "Arora",
    }
    return render(request, "base/pets.html", context)
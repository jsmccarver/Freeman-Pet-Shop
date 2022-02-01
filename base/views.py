from django.shortcuts import render
# Create your views here.
pets = [
        {'id': 1, 'name': 'Lets learn python!'},
        {'id': 2, 'name': 'Design with me'},
        {'id': 3, 'name': 'Frontend developers'},
    ]
def home(request):
    
    context = {'pets' : pets}
    return render(request, 'base/home.html', context)
    
def pet(request, pk):
    pet = None
    for i in pets:
        if i['id'] == int(pk):
            pet = i
    context = {'pet' : pet}
    return render(request, "base/pets.html", context)
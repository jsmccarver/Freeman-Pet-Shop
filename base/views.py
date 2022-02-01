from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name':'Lets Learn Python'},
    {'id': 2, 'name':'Design with me'},
    {'id': 3, 'name':'Frontend Developers'},

]

def home(request):
    context = {'rooms' : rooms}
    return render(request, 'home.html', context)
    
def rooms(request):
    return render(request, "room.html")
from django.shortcuts import render

#* Home Page View:
def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')



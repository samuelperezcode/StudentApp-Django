from django.shortcuts import render

rooms = [
    {'id': 1, "name":"Let's learn Python"},
    {'id': 2, "name":"Let's learn Javascript"},
    {'id': 3, "name":"Frontend Developers"},
]
#* Home Page View:
def home(request):
    context =  {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {"room":room}
    return render(request, 'base/room.html', context)



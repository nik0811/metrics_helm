# chat/views.py
from django.shortcuts import render


def SocketRoom(request, room_name):
    return render(request, 'user_list.html', {
        'room_name': room_name
    })


def Socket(request):
    return render(request, 'socket.html', context={'text': 'Hello World'})

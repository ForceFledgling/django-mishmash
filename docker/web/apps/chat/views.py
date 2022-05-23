import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    """Главная страница"""
    return render(request, 'chat/index.html', {})


# def room(request, room_name):
#     """Комната"""
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })

def room(request, room_name):
    """Комната"""
    return render(request, 'chat/room.html', {
        'app': f'{mark_safe(json.dumps("search"))}',
        'room_name_json': mark_safe(json.dumps(room_name)),
    })

def chat(message):
    
    return f'{message} - 123'
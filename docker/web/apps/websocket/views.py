from cgitb import reset
from email import message
import json
from unittest import result

from django.shortcuts import render
from django.utils.safestring import mark_safe

from apps.wiki.views import wiki

def websocket(app, username, message):
    '''
    Маршрутизируем входящее сообщение в нужное приложение
    Тут только дефолтные, остальноые в consumers в каждом приложении
    
    Самостоятельные приложения: чат.
    '''

    apps = {
        'wiki': wiki,
        # 'search': search,
    }

    if app in apps:
        return apps[app](app, username, message)
    else:
        return f'Приложение: {app}, Сообщение: {message} - нет инструкций!'
import json
from datetime import datetime

from apps.logging.views import log

from asgiref.sync import async_to_sync

from channels.exceptions import DenyConnection
from channels.generic.websocket import WebsocketConsumer

from django.contrib.auth.models import AnonymousUser

from portal.settings import global_variables

from .views import websocket

global_variables['used_channels'] = 0


class GlobalConsumer(WebsocketConsumer):

    def group_generation(self):
        '''
            Создает уникальную группу приложение-порльзователь-порт
            Переопределяется в разных приложениях
        '''
        self.app = self.scope['url_route']['kwargs']['app']
        self.user = self.scope["user"]
        self.port = self.scope['client'][1]
        self.group = f'group_{self.app}_{self.user}_{self.port}'

    def connect(self):
        '''
        Просьба не переопределять этот метод!!!!!!!!!
        Либо делайте проверку что пользователь залогинен!!!!
        '''

        apps_without_authentication = ['dismantling']

        if self.scope['user'] == AnonymousUser() and \
                self.scope['url_route']['kwargs']['app'] not in apps_without_authentication:
            log(
                self.scope["user"],
                self.scope['url_route']['kwargs']['app'],
                'Попытка запуска WebSocket со стороннего сайта, либо без учетной записи.',
            )
            raise DenyConnection("Такого пользователя не существует")

        # генерируем название локальной группы
        self.group_generation()

        # если пользователь залогинен подключаемся к глобальной группе
        async_to_sync(self.channel_layer.group_add)(
            'general',
            self.channel_name,
        )
        # подключаемся к группе
        async_to_sync(self.channel_layer.group_add)(
            self.group,
            self.channel_name,
        )

        # отправляем локальное сообщение о подключении
        self.connect_message()

        # отправляем глобальное сообщение о подключении
        self.broadcast_message_send('Подключился')

        global_variables['used_channels'] += 1
        self.accept()

    def connect_message(self):

        '''Дефолтное сообщение при подключении пользователя в группу'''

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'message_send',
                'message': f'{dt_string} - Дефолтное сообщение. Пользователь {self.user} открыл приложение \
                    {self.app}!\nЕго группа - {self.group}',
            },
        )

    def broadcast_message_send(self, message):
        self.app = self.scope['url_route']['kwargs']['app']
        if self.app != 'general':
            log(self.scope["user"], self.app, message)

        # async_to_sync(self.channel_layer.group_send)(
        #     'general',
        #     {
        #         'type': 'message_send',
        #         'message': f'{dt_string} - [BROADCAST] - <b>{self.user}</b> from {self.app} app!',
        #     }
        # )

    def disconnect(self, close_code):
        self.broadcast_message_send('Отключился')
        global_variables['used_channels'] -= 1
        async_to_sync(self.channel_layer.group_discard)(
            self.group,
            self.channel_name,
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        message = websocket(self.app, self.user, message)

        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'message_send',
                'message': message,
            },
        )

    def message_send(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'event': "Send",
            'message': message,
        }))

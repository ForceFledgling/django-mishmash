import json
from datetime import datetime

from apps.websocket.consumers import GlobalConsumer

from asgiref.sync import async_to_sync


class ChatConsumer(GlobalConsumer):

    def group_generation(self):
        '''Создаем группу по названию комнаты'''
        self.app = 'chat'
        self.user = self.scope["user"]
        self.port = self.scope['client'][1]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group = f'1group_chat_{self.room_name}'

    def connect_message(self):
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'message_send',
                'message': f'[{dt_string}] - Пользователь {self.user}_{self.port} вошел в комнату!',
            },
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # message = websocket(self.app, self.user, message)
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'message_send',
                'message': f'[{dt_string}] {self.user}: {message}',
            },
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group,
            self.channel_name,
        )

        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'message_send',
                'message': f'[{dt_string}] - Пользователь {self.user}_{self.port} отключился.',
            },
        )

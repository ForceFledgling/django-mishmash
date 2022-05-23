from apps.chat.consumers import ChatConsumer
from apps.websocket.consumers import GlobalConsumer
from apps.wiki.consumers import WikiConsumer

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import re_path


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/(?P<app>chat)/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
            re_path(r'ws/(?P<app>wiki)/(?P<page>\w+/)?$', WikiConsumer.as_asgi()),
            re_path(r'ws/(?P<app>\w+)/(?P<argument>\w+\/)?$', GlobalConsumer.as_asgi()),
            ],
        ),
    ),
    # 'channel': ChannelNameRouter({
    #     'test_print': PrintConsumer.as_asgi(),
    # }),
})

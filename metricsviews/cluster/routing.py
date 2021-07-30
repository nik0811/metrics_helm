from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    #re_path(r'api/view/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    path(r'api/view/clustersock/', consumers.ClsuterConsumer.as_asgi()),
]

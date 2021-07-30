from django.urls import path, re_path
from cluster.views.cluster import Cluster
from cluster.views.socket import Socket, SocketRoom

urlpatterns = [
     re_path(r'^cluster/', Cluster, name='cluster'),
     re_path(r'^socket/', Socket, name='socket'),
     path('<str:room_name>/', SocketRoom, name='room'),
]

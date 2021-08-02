from django.urls import path, re_path
from cluster.views.cluster import Cluster
from cluster.views.namespace import Namespace
from cluster.views.socket import Socket, SocketRoom

urlpatterns = [
     re_path(r'^cluster/', Cluster, name='cluster'),
     re_path(r'^socket/', Socket, name='socket'),
     re_path(r'^namespace/', Namespace, name='namespace'),
]

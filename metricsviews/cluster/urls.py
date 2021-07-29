from django.urls import path, re_path
from cluster.views.cluster import Cluster

urlpatterns = [
     re_path(r'^cluster/', Cluster, name='cluster'),
]

from django.urls import path, re_path
from cluster.views.cluster import Cluster
from cluster.views.namespace import Namespace, DeleteNamespace

urlpatterns = [
     re_path(r'^cluster/', Cluster, name='cluster'),
     re_path(r'^namespace/create', Namespace, name='namespace'),
     re_path(r'^namespace/delete', DeleteNamespace, name='deletenamespace'),
]

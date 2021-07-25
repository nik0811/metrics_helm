from django.urls import path, re_path
from . import views

urlpatterns = [
     path('api/nodes/', views.Nodes, name='nodes'),
]

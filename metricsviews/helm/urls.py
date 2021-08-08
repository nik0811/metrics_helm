from helm.views.chart import HelmRepo, HelmInstall, HelmList, HelmDelete, HelmHistory
from django.urls import path, re_path

urlpatterns=[
            re_path(r'^repo/', HelmRepo, name='helmrepo'),
            re_path(r'^install/', HelmInstall, name='helminstall'),
            re_path(r'^delete/', HelmDelete, name='helmdelete'),
            re_path(r'^list/', HelmList, name='helmlist'),
            re_path(r'^history/', HelmHistory, name='helmhistory'),
        ]

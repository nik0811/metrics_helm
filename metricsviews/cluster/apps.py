from django.apps import AppConfig


class ClusterConfig(AppConfig):
    name = 'cluster'
    def ready(self):
        import cluster.signals

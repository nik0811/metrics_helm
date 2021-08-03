from kubernetes import client, config
from django.conf import settings
core_api = None
apps_api = None
SSL = settings.K8S_SSL
API_KEY = None

def get_auth():
     
    global core_api
    if core_api == None:
        config.load_kube_config()
        if API_KEY is not None:
            configuration = client.Configuration()
            configuration.api_key['authorization'] = API_KEY
            configuration.api_key_prefix['authorization'] = 'Bearer'
            configuration.verify_ssl = SSL
            core_api = client.CoreV1Api(client.ApiClient(configuration))
        else:
            core_api = client.CoreV1Api()
    return core_api

def get_apps_auth():
    
    global apps_api
    if apps_api == None:
        config.load_kube_config()
        if API_KEY is not None:
            configuration = client.Configuration()
            configuration.api_key['authorization'] = API_KEY
            configuration.api_key_prefix['authorization'] = 'Bearer'
            configuration.verify_ssl = SSL
            apps_api = client.AppsV1Api(client.ApiClient(configuration))
        else:
            apps_api = client.AppsV1Api()
    return apps_api

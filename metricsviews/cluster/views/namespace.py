from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from kubernetes import client
from kubernetes.client.rest import ApiException
from pprint import pprint
from cluster.views.k8s import env
import urllib3
import logging
import re, json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

configuration = client.Configuration()
# Configure API key authorization: BearerToken
configuration.api_key['authorization'] = env.api_key
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = env.apiserver
configuration.username = "metricsviews"

configuration._preload_content=False

configuration.verify_ssl = False

ip_match = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

#@login_required(login_url="/login/")
@api_view(['POST'])
def Namespace(request):
    try:
        data = request.data
        namespace_name = data['namespace']
        try:
            with client.ApiClient(configuration) as api_client:

                namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace_name))

                # Create an instance of the API class
                api_instance = client.CoreV1Api(api_client)
                api_instance.create_namespace(namespace)
        except ApiException as e:
            return Response("{}".format(json.loads(e.body)), status=status.HTTP_403_FORBIDDEN)
        
        DATA={"Result": "Namespace Created: {}".format(namespace_name)}
        return (JsonResponse(DATA, safe=False))
    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)

#_namespaces = client.list_namespace(_request_timeout=3)
#if any(ns.metadata.name == namespace_name for ns in _namespaces.items):
#    DATA={"Result": "Namespace Created: {}".format(namespace_name)}
#    return (JsonResponse(DATA, safe=False))

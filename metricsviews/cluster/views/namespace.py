from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from kubernetes import client
from kubernetes.client.rest import ApiException
from cluster.k8s.k8s_auth import get_auth
import logging
import json

logger = logging.getLogger(__name__)

auth_api = get_auth()
#@login_required(login_url="/login/")
@api_view(['POST'])
def Namespace(request):
    try:
        data = request.data
        namespace_name = data['namespace']
        try:
            namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace_name))
            # Create an instance of the API class
            auth_api.create_namespace(namespace)
        except ApiException as e:
            return Response("{}".format(json.loads(e.body)), status=status.HTTP_403_FORBIDDEN)
        
        DATA={"Result": "Namespace Created: {}".format(namespace_name)}
        return (JsonResponse(DATA, safe=False))
    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def DeleteNamespace(request):
    try:
        data = request.data
        namespace_name = data['namespace']
        try:
            auth_api.delete_namespace(namespace_name)
            logger.info("Deleting namespace: {}".format(namespace_name))
        except ApiException as e:
            return Response("{}".format(json.loads(e.body)), status=status.HTTP_403_FORBIDDEN)
      
        DATA={"Result": "Namespace Deleted: {}".format(namespace_name)}
        return (JsonResponse(DATA, safe=False))
    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)

from kubernetes import client
from rest_framework.response import Response
from kubernetes.client.rest import ApiException
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from cluster.k8s.k8s_auth import get_auth
import re

auth_api = get_auth()
ip_match = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

#@login_required(login_url="/login/")
def Cluster(request):
    try:
        # Enter a context with an instance of the API kubernetes.client
        NODE_IP=[]
        NODE_NAME=[]
        try:
            api_response = auth_api.list_node()
            for stat in api_response.items:
                _stat=(stat.status.addresses[::-1])
                for addr in  _stat:
                    if ip_match.match(addr.address):
                        NODE_IP.append(addr.address)
                    else:
                        NODE_NAME.append(addr.address)
            NODES=(dict(zip(NODE_NAME, NODE_IP)))
            NODE_LEN={"Total_Node": len(NODE_IP)}
            DATA={**NODES, **NODE_LEN}
            return (JsonResponse(DATA))
        except ApiException as e:
            return Response("{}".format(json.loads(e.body)), status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)

from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pprint import pprint
from cluster.views.k8s import env
import urllib3
import logging
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

configuration = kubernetes.client.Configuration()
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
def Cluster(request):
    try:
        # Enter a context with an instance of the API kubernetes.client
        with kubernetes.client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = kubernetes.client.CoreV1Api(api_client)
            NODE_IP=[]
            NODE_NAME=[]
            try:
                api_response = api_instance.list_node()
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
from __future__ import print_function
from django.shortcuts import render
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from k8s import env
import urllib3
import json

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

# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.CoreV1Api(api_client)
    
    try:
        keys=['node-role.kubernetes.io/control-plane', 'node-role.kubernetes.io/master']
        api_response = api_instance.list_node()
        instance=api_instance.list_node()
        for label in range(len(api_response.items)):
            name=api_response.items[label].metadata.labels['kubernetes.io/hostname']
            instance=api_instance.read_node_status(name)
            pprint(instance.status.addresses)
            status=instance.status.conditions
            search_for_master=api_instance.read_node_status(name).metadata.labels
            if any(key in search_for_master for key in keys):
                #print('%s: master %s'%(name, status[-1].type))
                pass
            else:
                #print('%s: worker %s'%(name, status[-1].type))
                pass
        #pprint(instance.status.addresses)
        
    except ApiException as e:
        print("Exception when calling Api: %s\n" % e)

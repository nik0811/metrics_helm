from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
import subprocess
import json
from subprocess import check_output


@api_view(['POST'])
def HelmRepo(request):
    try:
        data = request.data
        chart_name = data['chart_name']
        chart_url  = data['chart_url']
        chart_action = data['chart_action']
        chart_to_remove = "helm repo remove %s"%(chart_name)
        chart_to_add = "helm repo add %s %s"%(chart_name, chart_url)
        chart_update = "helm repo update"
        chart_search = "helm search repo %s"%(chart_name)

        try:
            if chart_action == "delete":
                execute=(check_output(chart_to_remove.split(), stderr=subprocess.STDOUT)).decode().strip()
            elif chart_action == "add":
                execute=(check_output(chart_to_add.split(), stderr=subprocess.STDOUT)).decode().strip()
            elif chart_action == "update":
                execute=(check_output(chart_update.split(), stderr=subprocess.STDOUT)).decode().strip()
            elif chart_action == "search":
                execute=(check_output(chart_search.split(), stderr=subprocess.STDOUT)).decode().strip()
            else:
                return Response({'detail': 'Please Specify The Chart Action TO Either Add or Delete.'},status=status.HTTP_400_BAD_REQUEST)
        except subprocess.CalledProcessError as e:
            return Response("{}, (ErrorCode: {})".format((e.output).decode().strip(), e.returncode), status=status.HTTP_403_FORBIDDEN)
        
        DATA={"Result": execute}
        return (JsonResponse(DATA, safe=False))

    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def HelmInstall(request):

    try:
        data = request.data
        chart_name = data['chart_name']
        release_name = data['release_name']
        chart_action = data['chart_action']
        chart_namespace = data['chart_namespace']

        if (release_name == "False") and (chart_namespace == "False"):
            chart_install = "helm install {}/{} --generate-name".format(chart_name, chart_name)
        elif (release_name != "False") and (chart_namespace == "False"):
            chart_install = "helm install {}/{} --name-template {}".format(chart_name, chart_name, release_name)
        elif (release_name == "False") and (chart_namespace != "False"):
            chart_install = "helm install {}/{} --generate-name -n {}".format(chart_name, chart_name, chart_namespace)
        elif (release_name != "False") and (chart_namespace != "False"):
            chart_install = "helm install {}/{} --name-template {} -n {}".format(chart_name, chart_name, release_name, chart_namespace)

        try:
            if (chart_action == "install"):
                execute=(check_output(chart_install.split(), stderr=subprocess.STDOUT)).decode().strip()
            else:
                return Response({'detail': 'Please Provide The Correct Parameter To Perform The Installation Of Your Chart.'},status=status.HTTP_400_BAD_REQUEST)
        except subprocess.CalledProcessError as e:
            return Response("{}, (ErrorCode: {})".format((e.output).decode().strip(), e.returncode), status=status.HTTP_403_FORBIDDEN)

        DATA={"Result": execute}
        return (JsonResponse(DATA, safe=False))

    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def HelmDelete(request):

    try:
        data = request.data
        chart_action = data['chart_action']
        release_name = data['release_name']
        chart_namespace = data['chart_namespace']
        
        if (chart_namespace == "False"):
            chart_delete = "helm delete {}".format(release_name)
        elif (chart_namespace != "False"):
            chart_delete = "helm delete {} -n {}".format(release_name, chart_namespace)
        
        try:
            if (chart_action == "delete"):
                execute=(check_output(chart_delete.split(), stderr=subprocess.STDOUT)).decode().strip()
            else:
                return Response({'detail': 'Please Provide The Correct Parameter To Dlete Released Chart.'},status=status.HTTP_400_BAD_REQUEST)
        except subprocess.CalledProcessError as e:
            return Response("{}, (ErrorCode: {})".format((e.output).decode().strip(), e.returncode), status=status.HTTP_403_FORBIDDEN)

        DATA={"Result": execute}
        return (JsonResponse(DATA, safe=False))

    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def HelmList(request):
    try:
        data = request.data
        chart_action = data['chart_action']
        chart_list = "helm ls -A -o json"
        try:
            if (chart_action == "list"):
                execute=(check_output(chart_list.split(), stderr=subprocess.STDOUT)).decode().strip()
            else:
                return Response({'detail': 'Please Provide The Correct Parameter To List Chart.'},status=status.HTTP_400_BAD_REQUEST)
        except subprocess.CalledProcessError as e:
            return Response("{}, (ErrorCode: {})".format((e.output).decode().strip(), e.returncode), status=status.HTTP_403_FORBIDDEN)
        
        return (JsonResponse(json.loads(execute), safe=False))

    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)

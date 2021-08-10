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
        namespace = data['namespace']
        timeout = data['timeout']
        chart_path = data['chart_path']
        if (len(release_name) == 0) and (len(namespace.split()) == 0) and (len(chart_path.split()) == 0):
            chart_install = "helm install --timeout {}s {}/{} --generate-name".format(timeout, chart_name, chart_name)
        elif (len(release_name) > 0) and (len(namespace.split()) == 0) and (len(chart_path.split()) == 0):
            chart_install = "helm install --timeout {}s {}/{} --name-template {}".format(timeout, chart_name, chart_name, release_name)
        elif (len(release_name) == 0) and (len(namespace.split()) > 0) and (len(chart_path.split()) == 0):
            chart_install = "helm install --timeout {}s {}/{} --generate-name -n {}".format(timeout, chart_name, chart_name, chart_namespace)
        elif (len(release_name) > 0) and (len(namespace.split()) > 0) and (len(chart_path.split()) == 0):
            chart_install = "helm install --timeout {}s {}/{} --name-template {} -n {}".format(timeout, chart_name, chart_name, release_name, chart_namespace)
        elif (len(release_name) == 0) and (len(namespace.split()) == 0) and (len(chart_path.split()) > 0):
            chart_install = "helm install --timeout {}s --generate-name {}".format(timeout, chart_path)
        elif (len(release_name) > 0) and (len(namespace.split()) == 0) and (len(chart_path.split()) > 0):
            chart_install = "helm install --timeout {}s --name-template {} {}".format(timeout, release_name, chart_path)
        elif (len(release_name) == 0) and (len(namespace.split()) > 0) and (len(chart_path.split()) > 0):
            chart_install = "helm install --timeout {}s --generate-name -n {} {}".format(timeout, chart_namespace, chart_path)
        elif (len(release_name) > 0) and (len(namespace.split()) > 0) and (len(chart_path.split()) > 0):
            chart_install = "helm install --timeout {}s --name-template {} -n {} {}".format(timeout, release_name, chart_namespace, chart_path)

        try:
            if chart_install:
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
def HelmUpgrade(request):

    try:
        data = request.data
        release_name = data['release_name']
        timeout = data['timeout']
        chart_path = data['chart_path']
        if data['force'] == "false":
            chart_install = "helm upgrade --atomic --install --timeout {}s {} {}".format(timeout, release_name, chart_path)
        elif data['force'] == "true":
            chart_install = "helm upgrade --atomic --install --force --timeout {}s {} {}".format(timeout, release_name, chart_path)
        elif (len(data['version'].split()) > 0) and data['force'] == "true":
            chart_install = "helm upgrade --atomic --install --force --version {} --timeout {}s {} {}".format(version, timeout, release_name, chart_path)
        elif (len(data['version'].split()) > 0) and data['force'] == "false":
            chart_install = "helm upgrade --atomic --install --version {} --timeout {}s {} {}".format(version, timeout, release_name, chart_path)

        try:
            if chart_install:
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
def HelmRollback(request):

    try:
        data = request.data
        release_name = data['release_name']
        timeout = data['timeout']
        revision = data['revision']
        if data['force'] == "false":
            chart_install = "helm rollback --timeout {}s {} {}".format(timeout, release_name, revision)
        elif data['force'] == "true":
            chart_install = "helm rollback --force --timeout {}s {} {}".format(timeout, release_name, revision)

        try:
            if chart_install:
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
        release_name = data['release_name']
        namespace = data['namespace']
        keep_history = data['keep_history']
        if keep_history == "true":
            if (len(namespace.split()) == 0):
                chart_delete = "helm delete {} --keep-history".format(release_name)
            elif (len(namespace.split()) > 0):
                chart_delete = "helm delete {} -n {} --keep-history".format(release_name, namespace)
        elif keep_history == "false":
            if (len(namespace.split()) == 0):
                chart_delete = "helm delete {}".format(release_name)
            elif (len(namespace.split()) > 0):
                chart_delete = "helm delete {} -n {}".format(release_name, namespace)
        else:
            return Response({'detail': 'Please Provide The Correct Parameter For Keep History <true/false>'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if chart_delete:
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
        list_type = data['list_type']
        namespace = data['namespace']
        if list_type == "release" and (len(namespace.split()) == 0):
            chart_list = "helm ls -A -o json"
        elif list_type == "repo":
            chart_list = "helm repo ls -o json"
        elif (list_type == "release") and (len(namespace.split()) > 0):
            chart_list = "helm ls -n {} -o json".format(data['namespace'])
        else:
            return Response({'detail': 'Pass the correct parameter for repo_list, It will be either <release or repo>'},status=status.HTTP_400_BAD_REQUEST)
            
        try:
            if chart_list:
                execute=(check_output(chart_list.split(), stderr=subprocess.STDOUT)).decode().strip()
            else:
                return Response({'detail': 'Please Provide The Correct Parameter To List Chart.'},status=status.HTTP_400_BAD_REQUEST)
        except subprocess.CalledProcessError as e:
            return Response("{}, (ErrorCode: {})".format((e.output).decode().strip(), e.returncode), status=status.HTTP_403_FORBIDDEN)
        
        return (JsonResponse(json.loads(execute), safe=False))

    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def HelmHistory(request):
  
    try:
        data = request.data
        release_name = data['release_name']
        namespace = data['namespace']
        if (len(namespace.split()) == 0):
            chart_history = "helm history {} -o json".format(release_name)
        elif (len(namespace.split()) > 0):
            chart_history = "helm history {} -n {} -o json".format(release_name, namespace)
        else:
            return Response({'details': 'Pass the correct parameter either with namespcae or just pass empty string.'},status=status.HTTP_400_BAD_REQUEST)

        try:
            if chart_history:
                execute=(check_output(chart_history.split(), stderr=subprocess.STDOUT)).decode().strip()
            else:
                return Response({'detail': 'Please Provide The Release Name.'},status=status.HTTP_400_BAD_REQUEST)
        except subprocess.CalledProcessError as e:
            return Response("{}, (ErrorCode: {})".format((e.output).decode().strip(), e.returncode), status=status.HTTP_403_FORBIDDEN)

        return (JsonResponse(json.loads(execute), safe=False))

    except Exception as e:
        return Response({'detail':f'{e}'},status=status.HTTP_400_BAD_REQUEST)


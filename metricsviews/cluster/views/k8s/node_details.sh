#!/bin/bash
action=$1
if [[ '$action' == 'delete' ]]; then
	kind delete cluster --name milky
        kind create cluster --config kind.yaml --name milky
        kubectl apply -f cluster_rolebinding.yaml
        kubectl apply -f cluster_role.yaml
else
        CLUSTER_NAME=$(kubectl config view -o jsonpath='{range .clusters[*]}{.name}{end}')
        APISERVER=$(kubectl config view -o jsonpath="{.clusters[?(@.name==\"$CLUSTER_NAME\")].cluster.server}")
        TOKEN=$(kubectl get secrets -o jsonpath="{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='default')].data.token}"|base64 --decode)
        echo "api_key=\"$TOKEN\"" > env.py
        echo "apiserver=\"$APISERVER\"" >> env.py
        curl -X GET $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure
fi

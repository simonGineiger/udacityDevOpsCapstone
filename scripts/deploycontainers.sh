#!/bin/bash
aws eks update-kubeconfig --name UdacityDevOpsCapstoneK8S-Cluster
/home/ubuntu/bin/kubectl apply -f k8s/api_deployment.yml

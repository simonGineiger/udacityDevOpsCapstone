# this script uses cloudformation templates to create an EKS cluster and deploy a node group to it

import boto3
import json

eks_cluster_name = "eks-cluster"
eks_nodegroup_name = "eks-nodegroup"

cloudformation = boto3.client("cloudformation")
waiter = cloudformation.get_waiter('stack_create_complete')

with open("EKScluster.yml") as file:
    ClusterTemplateBody = file.read()
with open("EKSnodegroup.yml") as file:
    NodegroupTemplateBody = file.read()
with open("parameters.json") as file:
    Parameters = json.load(file)

# create EKS cluster

cluster_creation_response = cloudformation.create_stack(
    StackName=eks_cluster_name,
    TemplateBody=ClusterTemplateBody,
    Parameters=Parameters,
)

# wait until cluster responds

waiter.wait(
    StackName=eks_cluster_name,
    WaiterConfig={
        'Delay': 20,
        "MaxAttemps": 100
    }
)

print("cluster created")
print(cluster_creation_response)

# put nodegroup on cluster

nodegroup_creation_response = cloudformation.create_stack(
    StackName=eks_nodegroup_name,
    TemplateBody=NodegroupTemplateBody,
    Parameters=Parameters,
)

# wait until nodegroup responds

waiter.wait(
    StackName=eks_nodegroup_name,
    WaiterConfig={
        'Delay': 20,
        "MaxAttemps": 100
    }
)

print("nodegroup created")
print(nodegroup_creation_response)

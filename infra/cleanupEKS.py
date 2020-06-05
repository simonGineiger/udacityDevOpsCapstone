import boto3

eks_cluster_name = "eks-cluster"
eks_nodegroup_name = "eks-nodegroup"

cloudformation = boto3.client("cloudformation")
waiter = cloudformation.get_waiter("stack_delete_complete")

nodegroup_deletion_response = cloudformation.delete_stack(
    StackName=eks_nodegroup_name,
)

waiter.wait(
    StackName=eks_nodegroup_name,
    WaiterConfig={
        'Delay': 20,
        "MaxAttemps": 100
    }
)

print("nodegroup deleted")

cluster_deletion_response = cloudformation.delete_stack(
    StackName=eks_cluster_name,
)

waiter.wait(
    StackName=eks_cluster_name,
    WaiterConfig={
        'Delay': 20,
        "MaxAttemps": 100
    }
)

print("cluster deleted")
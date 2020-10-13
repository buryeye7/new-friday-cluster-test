This repository provides you with the convenient way to make the test evnvironment for Friday blockchain on AWS simply. 
The Friday nodes are going to run automatically after doing the procedure below.

Prerequsite
1. Install aws-cli.
2. Set the credentials of aws-cli to kops (IAM) 
    - Refer to kops/init-kops.sh.
3. Install kops.
4. Install kubectl.

Procedure
1. Run "./kops/make-cluster.sh create {kubernetes_node_number}", which is for creating the k8s nodes. If you want, you can edit the script to modify configuration of kubernetes. {kubernetes_node_number} must be greater than or equal to 6 and be a multiple of 3.
    Example)
    If {k8s_node_number} is 12,
    - Three nodes of them are assigned to Grafana, Prometheus, CouchDB respectively.
    - The remaining 9 nodes are used for friday nodes.

2. Open the following ports on the K8s nodes.
    - 30300, for the Grafana
    - 30990, for the Prometheus
    - 30598, for the CouchDB
    - 26660, for the Prometheus SRC Server
        
3. Run "./kubefiles/deploy-node.sh".

4. Run "./gaiapy/shot.sh".

If all procedures are successful, you can connect to {K8S_NODE_IP}:30300 and see the Grafana screen.

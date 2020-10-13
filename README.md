This repository provides you with the convenient way to make the test evnvironment for friday easiy. The Hdac nodes are going to run automatically after doing the procedure below.

Prerequsite

Install aws-cli.
Set the credentials of aws-cli to kops (IAM).
Install kops.
Install kubectl.
Procedure

Run "./kops/make-cluster.sh create", which is for creating the k8s nodes. If you want, you can edit the script to modify the instance type, instance number, etc.

Run "./kubefiles/make-hdac-node-desc.sh {NO}", which you have to replace {NO} to the number of hdac-nodes except seed node.

Run "kubectl get nodes", select the k8s node on which Grafana is going to run and replace the nodeName in kubefiles/grafana/grafana.yaml with selected one.

Run "./kubefiles/deploy-node.sh"

Access the public IP address of the k8s node on which Grafana container is running with the port 3000.

If all procedures are successful, you will see the Grafana screen.

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, VPC, PrivateSubnet, VPCPeering, VPCRouter, Nacl, NATGateway, RouteTable

with Diagram("SiC instances") as diag:
    with Cluster("Region-us-east-1"):
        with Cluster("vpc 172.18.200.0/23"):
            with Cluster("SecurityGroup2\nAllows only Egress traffic"):
                ic=EC2("InstanceC")
            with Cluster("SecurityGroup1\nAllows all egress and ingress traffic"):
                ia=EC2("InstanceA")
                ib=EC2("InstanceB")
        ia >> Edge(label="a to c expected to be blocked") >> ic
        ia >> Edge(label="a to b allowed") >> ib

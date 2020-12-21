from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB, VPC, PrivateSubnet, VPCPeering, VPCRouter, Nacl, NATGateway, RouteTable

with Diagram("VPC peering") as diag:
    with Cluster("Region-us-east-1"):
        with Cluster("vpc-0968e5182a833cf5f 172.16.0.0/16"):
            vpcr1=VPC("vpcr1")
            r1suba=PrivateSubnet("172.16.1.0/24")
            r1subb=PrivateSubnet("172.16.2.0/24")
            r1nacl=Nacl("Inbound:\nrule100 allow 18.205.7.57/32:22\nrule120 allow 172.16.2.0/24:0-65535\nrule123 allow 172.16.2.0/24:icmp\nrule133 allow 10.10.0.0/16:icmp\nOutbound\nrule100 allow -1 protocol 0.0.0.0/0")
            
        with Cluster("r1 SG\nSecurityGroupIngress:- IpProtocol: tcp\nFromPort: 22\nToPort: 22\nCidrIp: 0.0.0.0/0\n- IpProtocol: icmp\nFromPort: -1\nToPort: -1\nCidrIp: 0.0.0.0/0"):
            r1bastion=EC2("172.16.1.55")
            r1private=EC2("172.16.2.117")
            

        r1rtb=VPCRouter("rtb-0bf8eafe0d1c8f850")
            
    with Cluster("Region-us-east-2"):
        with Cluster("vpc-02cd39c06eefc11ed 10.10.0.0/16"):
            vpcr2=VPC("vpcr2")
            r2suba=PrivateSubnet("10.10.1.0/24")
            r2nacl=Nacl("Inbound:\nrule100 allow 172.16.0.0/16:22\nrule120 allow 172.16.0.0/16:icmp\nOutbound\nrule200 allow -1 protocol 0.0.0.0/0")

        with Cluster("r2 SG\nSecurityGroupIngress:\n- IpProtocol: tcp\nFromPort: 22\nToPort: 22\nCidrIp: 0.0.0.0/0\n- IpProtocol: icmp\nFromPort: -1\nToPort: -1\nCidrIp: 0.0.0.0/0\n"):
            r2private=EC2("10.10.1.8")

        r2rtb=VPCRouter("rtb-0cd90e8cf4d75fa1f")
    
    peer=VPCPeering("pcx-0e41ccd260c4c3dac")
    vpcr1 >> Edge(label="route table has\n10.10.0.0/16\ntarget: pcx-0e41ccd260c4c3dac\n172.16.0.0/16 target:local\n0.0.0.0/0\ntarget: igw-07d0775989748de46\n\nSubnets Associations:\n172.16.1.0/24\n172.16.2.0/24\nthese added via console") << peer >> Edge(label="route table has\n10.10.0.0/16 target: local\n172.16.0.0/16\ntarget: pcx-0e41ccd260c4c3dac\n\nSubnets Associations:\n10.10.1.0/24\nthese added via console") << vpcr2
diag
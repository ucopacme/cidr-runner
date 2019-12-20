(python3.7) agould@horus:~/git-repos/github/ucopacme/cidr-runner> ec2-instance-list
jhsu-vpcA1-10.48.40.27
i-0d9b6d3da8f215fd5
10.48.40.27
54.186.153.159
running

jhsu-vpcA2-10.48.40.83
i-0be0e0467b7bb2bc3
10.48.40.83
34.221.182.252
running

jhsu-128-48-110-7
i-0954c629ea593aa40
128.48.110.7
52.33.65.210
running

jhsu-128-48-110-4
i-0f559c7b046588ba2
128.48.110.4
18.236.187.229
running

csr-jhsu-172-16-100-32
i-01fec2cdecabf91b7
172.16.100.43
null
stopped

fms-test
i-0f529c8e35f256d43
172.16.100.85
null
running

----

> aws ec2 describe-vpcs | jq -r '.Vpcs[] | .CidrBlock, .VpcId, .State, (.Tags[] | select(.Key == "Name") | .Value) ,""'
172.16.100.0/24
vpc-0445c3e4965913f6d
available
vpc-172-16-100-0

172.31.0.0/16
vpc-6b548a13
available
Default VPC

128.48.110.0/24
vpc-0c335189e74a744ed
available
NatStack-NetProd/VpcNat

10.48.40.0/26
vpc-09567b53581f3e7e3
available
TgwaitStack-A1-10.48.40.0-26

10.48.40.64/26
vpc-0b3e9d2036036b532
available
TgwaitStack-A1-10.48.40.64-26

----

> aws ec2 describe-vpn-connections | jq -r '.VpnConnections[] | .VpnConnectionId, .VpnGatewayId, .CustomerGatewayId, .Routes[].DestinationCidrBlock, (.Tags[] | select(.Key == "Name") | .Value), ""'
vpn-0cd35dd3440be7607
vgw-0d91d8875d363cfe9
cgw-075f6ff6b0ba84372
128.48.202.0/24
tgwait-vpn-vpcA1-10.48.40.64-26

vpn-02b4fc9ab91595100
null
cgw-05fc6434e0f7cfc76
tgw-net-prod-vpn

vpn-0e21d982a466d694d
null
cgw-05fc6434e0f7cfc76
tgwait-vpn-test

vpn-072d163d1e6f674f2
null
cgw-05fc6434e0f7cfc76
tgwait-vpn-202.0

vpn-0880fc46feae89925
vgw-030d7be7ecc3d4862
cgw-05fc6434e0f7cfc76
128.48.202.158/32
128.48.202.0/24
tgwait-vpn-vpcA1-10.48.40.0-26


----

> aws ec2 describe-transit-gateways | jq -r '.TransitGateways[]| .TransitGatewayId, .State, .Description, (.Tags[] | select(.Key == "Name") | .Value), ""'
tgw-035b9cea527f0e86e
available
UCOP Organizational Transit Gateway
tgw-net-prod

tgw-03e59dafb0e4e761c
available
TGW in net-prod
tgwait-tgw

-----


> aws ec2 describe-transit-gateway-vpc-attachments | jq -r '.TransitGatewayVpcAttachments[] | select(.TransitGatewayId == "tgw-035b9cea527f0e86e") | .TransitGatewayAttachmentId, .TransitGatewayId, .VpcId, .VpcOwnerId, .State, (.Tags[] | select(.Key == "Name") | .Value), ""'
tgw-attach-03fb681520a03fc30
tgw-035b9cea527f0e86e
vpc-095addf5ae2f29dc7
071826132890
available
ait-training-d1-test

tgw-attach-05b528a1a7f2dd0fa
tgw-035b9cea527f0e86e
vpc-0bcd987dd82423171
041008331506
available
Seg-Log-10.48.43.0-26

tgw-attach-070f73dd537ff599c
tgw-035b9cea527f0e86e
vpc-0a78156cf7c52c476
863914007401
available
ucpath-build-128.48.255.128/27

tgw-attach-07810494cb85f01a2
tgw-035b9cea527f0e86e
vpc-0ff104e65ec70d47f
111569475818
available
ucpath-pmo-128.48.66.160/27

tgw-attach-08c1413c8b23dc9a9
tgw-035b9cea527f0e86e
vpc-0f2ab9f69fe9bde46
217985836260
available
ait-poc-c1-test

tgw-attach-0e399e7c33ac191ba
tgw-035b9cea527f0e86e
vpc-965f12f0
863914007401
available
ucpath-build-10.48.160.0/20

tgw-attach-0e52c57d2818b5c4e
tgw-035b9cea527f0e86e
vpc-0496747e4bed10360
011208821250
available
ucpath-prod-128.48.66.192/27



TGW_ID=tgw-03e59dafb0e4e761c
TGW_ID=tgw-035b9cea527f0e86e

aws ec2 describe-transit-gateway-vpc-attachments | jq -r '.TransitGatewayVpcAttachments[] | select(.TransitGatewayId == "tgw-03e59dafb0e4e761c") | .TransitGatewayAttachmentId, .TransitGatewayId, .VpcId, .VpcOwnerId, .State, (.Tags[] | select(.Key == "Name") | .Value), ""'
tgw-attach-0158604a9c4621a5f
tgw-03e59dafb0e4e761c
vpc-0bcd987dd82423171
041008331506
available
tgwait-vpcS1

tgw-attach-03f0b424a2f82ab68
tgw-03e59dafb0e4e761c
vpc-02e0667b6871f5726
217985836260
available
tgwait-vpcC2

tgw-attach-073f48bfd2e690c05
tgw-03e59dafb0e4e761c
vpc-0f2ab9f69fe9bde46
217985836260
available
tgwait-vpcC1

tgw-attach-0c0d1826b393542f9
tgw-03e59dafb0e4e761c
vpc-095addf5ae2f29dc7
071826132890
available
tgwait-vpcD1

tgw-attach-0d5827f3c695b7c9d
tgw-03e59dafb0e4e761c
vpc-0b3e9d2036036b532
443591488593
available
tgwait-vpcA2

-----


aws ec2 describe-transit-gateway-route-tables | jq -r '.TransitGatewayRouteTables[] | select(.TransitGatewayId == "tgw-03e59dafb0e4e761c") | .TransitGatewayRouteTableId, .TransitGatewayId, .State, (.Tags[] | select(.Key == "Name") | .Value), ""'

tgw-rtb-00129dfaea1dd56ad
tgw-03e59dafb0e4e761c
available
tgwait-rtb-C2

tgw-rtb-018364b0215ab973a
tgw-03e59dafb0e4e761c
available
tgwait-rtb-D1

tgw-rtb-02143f1921c95123b
tgw-03e59dafb0e4e761c
available
tgwait-rtb-C1

tgw-rtb-0a420f87f2c3a78e2
tgw-03e59dafb0e4e761c
available
tgwait-rtb-vpn-jj

tgw-rtb-0a64db1ed36f6347c
tgw-03e59dafb0e4e761c
available
tgwait-rtb-A1

tgw-rtb-0aaf5531e9f37dda3
tgw-03e59dafb0e4e761c
available
tgwait-rtb-S1

tgw-rtb-0d2307087ee8caa91
tgw-03e59dafb0e4e761c
available
tgwait-rtb-vpn-202.0

tgw-rtb-0d9e67e617a9c7767
tgw-03e59dafb0e4e761c
available
tgwait-rtb-A2-vpn-test


aws ec2 describe-transit-gateway-route-tables | jq -r '.TransitGatewayRouteTables[] | select(.TransitGatewayId == "tgw-03e59dafb0e4e761c") | .TransitGatewayRouteTableId'
tgw-rtb-00129dfaea1dd56ad
tgw-rtb-018364b0215ab973a
tgw-rtb-02143f1921c95123b
tgw-rtb-0a420f87f2c3a78e2
tgw-rtb-0a64db1ed36f6347c
tgw-rtb-0aaf5531e9f37dda3
tgw-rtb-0d2307087ee8caa91
tgw-rtb-0d9e67e617a9c7767

for route in $(aws ec2 describe-transit-gateway-route-tables | jq -r '.TransitGatewayRouteTables[] | select(.TransitGatewayId == "tgw-03e59dafb0e4e761c") | .TransitGatewayRouteTableId'); do
echo $route
done
tgw-rtb-00129dfaea1dd56ad
tgw-rtb-018364b0215ab973a
tgw-rtb-02143f1921c95123b
tgw-rtb-0a420f87f2c3a78e2
tgw-rtb-0a64db1ed36f6347c
tgw-rtb-0aaf5531e9f37dda3
tgw-rtb-0d2307087ee8caa91
tgw-rtb-0d9e67e617a9c7767

-----

> aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id tgw-rtb-00129dfaea1dd56ad --filter Name=state,Values=active
{
    "Routes": [
        {
            "DestinationCidrBlock": "10.48.41.0/26",
            "TransitGatewayAttachments": [
                {
                    "ResourceId": "vpc-0f2ab9f69fe9bde46",
                    "TransitGatewayAttachmentId": "tgw-attach-073f48bfd2e690c05",
                    "ResourceType": "vpc"
                }
            ],
            "Type": "propagated",
            "State": "active"
        },
        {
            "DestinationCidrBlock": "10.48.43.0/26",
            "TransitGatewayAttachments": [
                {
                    "ResourceId": "vpc-0bcd987dd82423171",
                    "TransitGatewayAttachmentId": "tgw-attach-0158604a9c4621a5f",
                    "ResourceType": "vpc"
                }
            ],
            "Type": "propagated",
            "State": "active"
        }
    ],
    "AdditionalRoutesAvailable": false
}

ROUTE_TABLES=$(aws ec2 describe-transit-gateway-route-tables | jq -r '.TransitGatewayRouteTables[] | select(.TransitGatewayId == "tgw-03e59dafb0e4e761c") | .TransitGatewayRouteTableId'
)
for route in $ROUTE_TABLES; do
  echo $route
  aws ec2 search-transit-gateway-routes --transit-gateway-route-table-id $route --filter Name=state,Values=active | jq -r '.Routes[].DestinationCidrBlock'
  echo
done 
tgw-rtb-00129dfaea1dd56ad
10.48.41.0/26
10.48.43.0/26

tgw-rtb-018364b0215ab973a
10.48.43.0/26

tgw-rtb-02143f1921c95123b
10.48.41.0/26
10.48.41.64/26
10.48.43.0/26

tgw-rtb-0a420f87f2c3a78e2
10.48.40.64/26

tgw-rtb-0a64db1ed36f6347c
10.48.40.64/26
10.48.43.0/26

tgw-rtb-0aaf5531e9f37dda3
10.48.40.64/26
10.48.41.0/26
10.48.41.64/26
10.48.42.0/26

tgw-rtb-0d2307087ee8caa91
10.48.40.64/26
10.48.41.0/26
10.48.41.64/26
10.48.42.0/26
10.48.43.0/26

tgw-rtb-0d9e67e617a9c7767
10.48.40.64/26
10.48.43.0/26



import boto3

import util


def describe_vpcs(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    paganator = util.paginate(client, client.describe_vpcs)
    return dict(Vpcs=[resource for resource in paganator])


def describe_subnets(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    paganator = util.paginate(client, client.describe_subnets)
    return dict(Subnets=[resource for resource in paganator])


def describe_route_tables(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    paganator = util.paginate(client, client.describe_route_tables)
    return dict(RouteTables=[resource for resource in paganator])


def describe_internet_gateways(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    paganator = util.paginate(client, client.describe_internet_gateways)
    return dict(InternetGateways=[resource for resource in paganator])


def describe_nat_gateways(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    paganator = util.paginate(client, client.describe_nat_gateways)
    return dict(NatGateways=[resource for resource in paganator])



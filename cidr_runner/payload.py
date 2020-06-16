import boto3

from cidr_runner import util


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


def network_data(region, account):
    '''
    The repetition within this function suggests using a loop whcih
    traverses a list of dictionary: {cmd: describe_vpcs, label: Vpcs}
    '''
    network_data = {}
    client = boto3.client('ec2', region_name=region, **account.credentials)
    paganator = util.paginate(client, client.describe_vpcs)
    network_data['Vpcs'] = [resource for resource in paganator]
    paganator = util.paginate(client, client.describe_subnets)
    network_data['Subnets'] = [resource for resource in paganator]
    paganator = util.paginate(client, client.describe_route_tables)
    network_data['RouteTables'] = [resource for resource in paganator]
    paganator = util.paginate(client, client.describe_internet_gateways)
    network_data['InternetGateways'] = [resource for resource in paganator]
    paganator = util.paginate(client, client.describe_nat_gateways)
    network_data['NatGateways'] = [resource for resource in paganator]
    return network_data



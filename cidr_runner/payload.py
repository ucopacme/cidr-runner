import boto3


def vpc_data(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    response = client.describe_vpcs()
    #response.pop('ResponseMetadata')
    #response['account_name'] = account.name
    #response['account_id'] = account.id
    #response['region'] = region
    #return response
    vpc_data = []
    for vpc in response['Vpcs']:
        vpc['AccountName'] = account.name
        vpc['Region'] = region
        vpc_data.append(vpc)
    return vpc_data

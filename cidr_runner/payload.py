import boto3


def vpc_data(region, account):
    client = boto3.client('ec2', region_name=region, **account.credentials)
    response = client.describe_vpcs()
    response.pop('ResponseMetadata')
    return response

    #print(response)
    return response['Vpcs']

import sys
from datetime import datetime
import boto3
import yaml


def paginate(client, method, **kwargs):
    paginator = client.get_paginator(method.__name__)
    for page in paginator.paginate(**kwargs).result_key_iters():
        for result in page:
            yield result


def yamlfmt(obj):
    if isinstance(obj, str):
        return obj
    try:
        return yaml.dump(obj, default_flow_style=False)
    except Exception:  # pragma: no cover
        return yaml.dump(str(obj))


def timestamp():
    return datetime.utcnow().isoformat()


def set_base_object_path():
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    return '{}/{}/{}'.format(year, month, day)


# TODO: syntax check scanned config data
def load_config(config_file):
    '''
    config_file is a open file object

    regions: []
    accounts: []
    reporting_account: ''
    reporting_region: ''
    bucket_name: ''
    payloads: []

    '''
    try:
        config = yaml.safe_load(config_file.read())
    except (yaml.scanner.ScannerError, UnicodeDecodeError):
        sys.exit("{} not a valid yaml file".format(config_file.name))
    return config


def setup_s3_bucket(config, crawler):
    account = crawler.org.get_account(config['reporting_account'])
    bucket_name = config['bucket_name'] + '-' + account.id
    s3_client = boto3.client('s3',
        region_name=config['reporting_region'],
        **account.credentials,
    )
    try:
        s3_client.create_bucket(
            ACL = 'private',
            Bucket = bucket_name,
            CreateBucketConfiguration = {'LocationConstraint': config['reporting_region']}
        )
    except s3_client.exceptions.BucketAlreadyOwnedByYou as e:
        pass
    s3 = boto3.resource('s3', **account.credentials)
    return s3.Bucket(bucket_name)


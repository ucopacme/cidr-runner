import sys
from datetime import datetime
import boto3
import yaml


def paginate(client, method, **kwargs):
    paginator = client.get_paginator(method.__name__)
    for page in paginator.paginate(**kwargs).result_key_iters():
        for result in page:
            yield result


def timestamp():
    return datetime.utcnow().isoformat()


def set_base_object_path(payload_title):
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    return '{}/{}/{}/{}'.format(payload_title, year, month, day)


def load_config(config_file):
    '''
    config_file is a open file object
    '''
    try:
        config = yaml.safe_load(config_file.read())
    except (yaml.scanner.ScannerError, UnicodeDecodeError):
        sys.exit("{} not a valid yaml file".format(config_file.name))
    return config


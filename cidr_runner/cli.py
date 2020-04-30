#!/usr/bin/env python

import io
import os
import sys

import yaml
import json
import boto3
from botocore.exceptions import ClientError
import click

import orgcrawler
from orgcrawler.utils import jsonfmt, yamlfmt
from orgcrawler.cli.utils import (
    setup_crawler,
)
import payload
import util


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--master-role', '-r',
    required=True,
    help='IAM role to assume for accessing AWS Organization Master account.'
)
@click.option('--config-file', '-f',
    default=os.path.expanduser("~/.cidr_runner/config.yaml"),
    show_default=True,
    type=click.File('r'),
    help='Path to file containing account/region specifications.'
)
def main(master_role, config_file):
    """
    Generate a list of AWS CIDR blocks in VPCs. Ignores default VPCs.

    Usage:

      ./cidr_runner.py -r MyIamRole -f config.yaml | tee output.yaml
    """

    #print(config_file)
    config = util.load_config(config_file)
    print(config)
    crawler = setup_crawler(
        master_role,
        accounts=config['accounts'],
        regions=config['regions'],
    )
    #print(yamlfmt([a.dump() for a in crawler.accounts]))

    execution = crawler.execute(
        payload.vpc_data,
    )
    #click.echo(jsonfmt(format_responses(execution)))
    text_stream = io.StringIO()
    for response in execution.responses:
        text_stream.write(jsonfmt(response.dump()) + '\n')
    #print(text_stream.getvalue())

    s3 = boto3.resource('s3')
    bucket = config['bucket_name']
    base_path = util.set_base_object_path()

    obj_path = base_path + '/' + 'vcp_data.json'
    print(obj_path)

    account = crawler.org.get_account(config['reporting_account'])
    bucket_name = config['bucket_name'] + '-' + account.id
    print(bucket_name)
    s3_client = boto3.client('s3', region_name=config['reporting_region'], **account.credentials)
    try:
        s3_client.create_bucket(
            ACL = 'private',
            Bucket = bucket_name,
            CreateBucketConfiguration = {'LocationConstraint': config['reporting_region']}
        )
    except s3_client.exceptions.BucketAlreadyOwnedByYou as e:
        pass

    s3_client.put_object(
        Bucket = bucket_name,
        Key = obj_path,
        Body = text_stream.getvalue(),
    )


'''
    try:
        s3.Object(bucket, obj).put(Body=text_stream.getvalue())
    except s3.meta.client.exceptions.NoSuchBucket as e:
        boto3.client('s3').create_bucket(
            ACL = 'private',
            Bucket = bucket,
            CreateBucketConfiguration = {'LocationConstraint':'us-west-2'}
        )
        s3.Object(bucket, obj).put(Body=text_stream.getvalue())

'''

if __name__ == '__main__':
    main()

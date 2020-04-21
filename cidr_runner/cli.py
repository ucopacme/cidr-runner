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
    format_responses,
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
    #print(yamlfmt(execution.dump()))
    # flatten responses into list of vpc 
    vpc_data = []
    for r in execution.responses:
        vpc_data += r.payload_output
    #print(yamlfmt(vpc_data))

    # extract cidr block associations
    #cidr_blocks = []
    text_stream = io.StringIO()
    for vpc in vpc_data:
        if not vpc['IsDefault']:
            for cidr in vpc['CidrBlockAssociationSet']:
                if cidr['CidrBlockState']['State'] == 'associated':
                    cidr_block = dict(
                        AccountId = vpc['OwnerId'],
                        AccountName = vpc['AccountName'],
                        Region = vpc['Region'],
                        VpcId = vpc['VpcId'],
                        CidrBlock = cidr['CidrBlock'],
                    )
                    #cidr_blocks.append(cidr_block)
                    text_stream.write(json.dumps(cidr_block) + '\n')
    #click.echo(yamlfmt(cidr_blocks))
    #print(text_stream.getvalue())
'''

    s3 = boto3.resource('s3')
    bucket = config['bucket_name']
    base_path = util.set_base_object_path('vpc_data')

    obj = base_path + '/' + 'cidr_blocks.json'
    print(obj)
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
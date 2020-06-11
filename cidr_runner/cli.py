#!/usr/bin/env python

import os
import sys
import json

import boto3
from botocore.exceptions import ClientError
import click

import orgcrawler
from orgcrawler.utils import jsonfmt
from orgcrawler.cli.utils import setup_crawler
import payload
import util


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--master-role', '-r',
    required=True,
    help='IAM role to assume for accessing AWS Organization Master account.'
)
@click.option('--config-file', '-f',
    default=os.path.expanduser("~/.config/cidr-runner.yaml"),
    show_default=True,
    type=click.File('r'),
    help='Path to file containing account/region specifications.'
)
def main(master_role, config_file):
    """
    Usage:

      ./cli.py -r MyIamRole -f cidr-runner.yaml
    """

    config = util.load_config(config_file)
    crawler = setup_crawler(
        master_role,
        accounts=config['accounts'],
        regions=config['regions'],
    )
    s3_bucket = util.setup_s3_bucket(config, crawler)
    base_obj_path = util.set_base_object_path()

    for payload_name in config['payloads']:
        #print('runnning payload: {}'.format(payload_name))

        obj_path = base_obj_path + '/' + payload_name + '.json'
        f = eval('payload.' + payload_name)
        execution = crawler.execute(f)

        text_stream = io.StringIO()
        for response in execution.responses:
            text_stream.write(jsonfmt(response.dump()) + '\n')
        s3_bucket.put_object(Key = obj_path, Body = text_stream.getvalue())


if __name__ == '__main__':
    main()


cidr_runner
===========

An orgcrawler app for gathering network resource configuration data
across all accounts in an AWS Organization and loading this data into
structured Athena Tables.

``cidr_runner`` is a component of the WeedNix AWS network admistration suite of tools.


Objective
---------

- Provide a framework running orgcrawler payload functions and posting 
  payload execution output into S3.

- Provide orgcrawler payload functions to collect the following resource
  configuration data:

  - VPC and subnets
  - VPNs
  - VPC Peering connections
  - TrasitGateways
  - DirectConnects

- Perform ETL on payload output into AWS Athena.

- Automate data collection and ETL



Installation
------------

Initally, install from git repo::

  pip install https://github.com/weednix/cidr_runner/archive/master.zip

this pa
 of all cidr blocks within an AWS organization.


Usage
-----

::

  cidr_runner -r MyIamRole -f path/to/myorg.yaml

this creates s3 bucket.  to create athena table `cidrblocks` from this bucket use `create_table.sql`


S3 Object Key Layout
--------------------

/payload-name/account_id/region/year/month/day/time/object_name

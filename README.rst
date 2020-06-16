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

  Current:

  - VPC and subnets

  Future:

  - VPNs
  - VPC Peering connections
  - TrasitGateways
  - DirectConnects




Installation
------------

Install from git repo::

  pip install https://github.com/weednix/cidr-runner/archive/master.zip

or to install an editable copy::

  git clone https://github.com/weednix/cidr-runner.git
  cd cidr-runner
  git install -3 .


Configuration
-------------

Create cidr-runner.yaml config file locally.  By default cidrrunner looks for this file in ``~/.config/cidr-runner.yaml``

Example::

(py3) MacBook-Pro:cidr-runner agould$ cat ~/.config/cidr-runner.yaml
  regions:
  - us-west-2
  - us-east-2
  accounts:
  - master
  - blee-poc
  - blee-dev
  - blee-prod
  - test2
  reporting_account: test2
  reporting_region: us-west-2
  bucket_name: cidrrunner
  payloads:
  - network_data



Usage
-----

cidrrunner requires IAM permissions to assume role in all Organization
accounts.  This role must have read access to all AWS network resources.

::

  (py3) MacBook-Pro:cidr-runner agould$ cidrrunner --help
  Usage: cidrrunner [OPTIONS]
  
    Usage:
  
      cidrrunner -r MyIamRole -f ~/.config/cidr-runner.yaml
  
  Options:
    -r, --master-role TEXT      IAM role to assume for accessing AWS
                                Organization Master account.  [required]
  
    -f, --config-file FILENAME  Path to file containing account/region
                                specifications.  [default:
                                /Users/agould/.config/cidr-runner.yaml]
  
    -h, --help                  Show this message and exit.
  


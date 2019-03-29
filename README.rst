cidr_runner
===========

an orgcrawler app for generating athena table of all cidr blocks within an AWS organization.


Usage
-----

::

  cidr_runner -r MyIamRole -f path/to/myorg.yaml

this creates s3 bucket.  to create athena table `cidrblocks` from this bucket use `create_table.sql`


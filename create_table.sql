CREATE EXTERNAL TABLE IF NOT EXISTS cidrblocks (
  AccountId string,
  AccountName string,
  CidrBlock string,
  Region string,
  VpcId string
)
ROW FORMAT serde 'org.openx.data.jsonserde.JsonSerDe'
with serdeproperties ( 'paths'='accountid, accountname, cidrblock, region, vpcid' )
LOCATION 's3://vpc-data-29fhlek/cidrrunner';

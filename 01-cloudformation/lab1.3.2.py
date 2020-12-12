import logging
import boto3
import json
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

client= boto3.client("sts")

with open('lab1.3.1.regionlist.json') as data_file:    
    data = json.load(data_file)
for region in data['region']:
    bucket_name = region + "-" + client.get_caller_identity()["Account"] + "-fiendly-name-jmd-020201212"
    print (bucket_name)
    create_bucket(bucket_name, region=None)
    
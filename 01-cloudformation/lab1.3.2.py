import logging
import boto3
import json
from botocore.exceptions import ClientError

def check_status( cf_client, stack_name ):
    lo_stacks = cf_client.describe_stacks(StackName=stack_name)["Stacks"]
    # la_stack = lo_stacks[0]
    # lc_cur_status = la_stack["StackStatus"]
    # print("Current status of stack " + la_stack["StackName"] + ": " + lc_cur_status)
    print("Current status of stack " + lo_stacks[0]["StackName"] + ": " + lo_stacks[0]["StackStatus"])

    return lo_stacks[0]["StackStatus"]


client_sts= boto3.client("sts")

with open('lab1.3.1.regionlist.json') as data_file:    
    data = json.load(data_file)

for region in data['region']:
    bucket_name = region + "-" + client_sts.get_caller_identity()["Account"] + "-fiendly-name-jmd-020201212"
    print (bucket_name)
    # create_bucket(bucket_name, region=None)
    cf_client = boto3.client('cloudformation', region)
    check_status( cf_client, stack_name="jmd-020201211-008" )    
import logging
import boto3
import json
from botocore.exceptions import ClientError
from pathlib import Path

def status_cnf( cf_client, stack_name ):
    stacks_cnf = cf_client.describe_stacks(StackName=stack_name)["Stacks"]
    print("Current status of stack " + stacks_cnf[0]["StackName"] + ": " + stacks_cnf[0]["StackStatus"])

    return stacks_cnf[0]["StackStatus"]

def create_cnf( cf_client, stack_name ):
    result_cnf = cf_client.create_stack(StackName=stack_name, TemplateBody=cnf_template)
    print("Output from API call: ")
    print(result_cnf)

def update_cnf( cf_client, stack_name ):
    try:
      result_cnf = cf_client.update_stack(StackName=stack_name, TemplateBody=cnf_template)
    except: 
      print ("something happened with the update")
    else:
      print("Output from Update: ")
      print(result_cnf)

def delete_cnf( cf_client, stack_name ):
    result_cnf = cf_client.delete_stack(StackName=stack_name)
    print("Output from API call: ")
    print(result_cnf)

client_sts= boto3.client("sts")

with open('lab1.3.1.regionlist.json') as data_file:    
    data = json.load(data_file)

cnf_template = Path('lab1.3.1.s3.yml').read_text()
action = "delete"
#action = "create"
name_cnf="jmd-020201213-003"

for region in data['region']:
    cf_client = boto3.client('cloudformation', region)

    try:
      status_cnf( cf_client, stack_name=name_cnf )
    except:
      if "delete" in action:     
        print("CNF is not defined and action is " + action + " so not creating the stack")
      else:     
        print("CNF is not defined should run a create stack")
        create_cnf( cf_client, stack_name=name_cnf )
    else:
      if "delete" in action:     
        print("CNF is defined and action is " + action + " going to remove the stack")
        delete_cnf( cf_client, stack_name=name_cnf )
      else:
        print("CNF is defined should run an update")
        update_cnf( cf_client, stack_name=name_cnf )

# list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    if "fiendly-name" in bucket["Name"]:
      print(f'  {bucket["Name"]}')
    # if "jmd" in bucket["Name"]:
    #   print(f'  {bucket["Name"]}')
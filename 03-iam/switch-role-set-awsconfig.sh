#!/bin/bash
set -e
creds_json=$(aws sts assume-role --role-arn arn:aws:iam::324320755747:role/su-jdlabs-321 --role-session-name lab321 --profile temp); break;;

aws configure set aws_access_key_id $(echo "$creds_json" | jq .Credentials.AccessKeyId |tr -d '"') --profile temprole
aws configure set aws_secret_access_key $(echo "$creds_json" | jq .Credentials.SecretAccessKey| tr -d '"') --profile temprole
aws configure set aws_session_token $(echo "$creds_json" | jq .Credentials.SessionToken|tr -d '"') --profile temprole

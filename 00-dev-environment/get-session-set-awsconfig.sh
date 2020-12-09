#!/bin/bash
creds_json=$(aws sts get-session-token  --serial-number  arn:aws:iam::324320755747:mfa/jason.davis.labs --token-code $1)
export AWS_ACCESS_KEY_ID=$(echo "$creds_json" | jq .Credentials.AccessKeyId |tr -d '"')
export AWS_SECRET_ACCESS_KEY=$(echo "$creds_json" | jq .Credentials.SecretAccessKey| tr -d '"')
export AWS_SESSION_TOKEN=$(echo "$creds_json" | jq .Credentials.SessionToken|tr -d '"')
export SERVICE_REGION=us-east-1

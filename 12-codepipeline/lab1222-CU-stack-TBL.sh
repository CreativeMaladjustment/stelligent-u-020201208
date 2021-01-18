#!/bin/bash
set -e

export STACKNAME=${STACKNAME:-jmd-020210118-DB1-001}
export STACKARN=`aws cloudformation describe-stacks --stack-name $STACKNAME | jq .Stacks[].StackId | tr -d '"'`

if [[ "$STACKARN" == *"cloudformation"* ]]; then
  echo "update $STACKARN"
else 
  echo "create $STACKNAME"
fi


# while true; do
#   read -p "MFA token:" mfa_token
#   case $mfa_token in
#     [0-9][0-9][0-9][0-9][0-9][0-9] ) creds_json=$(aws sts get-session-token  --serial-number  arn:aws:iam::324320755747:mfa/jason.davis.labs --token-code $mfa_token); break;;
#     * ) echo "Please enter 6-digit mfa token." ;;
#   esac
# done

# aws configure set aws_access_key_id $(echo "$creds_json" | jq .Credentials.AccessKeyId |tr -d '"') --profile temp
# aws configure set aws_secret_access_key $(echo "$creds_json" | jq .Credentials.SecretAccessKey| tr -d '"') --profile temp
# aws configure set aws_session_token $(echo "$creds_json" | jq .Credentials.SessionToken|tr -d '"') --profile temp


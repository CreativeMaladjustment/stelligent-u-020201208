#!/bin/bash
set -e
regionlist=$(jq -r '.region[]' lab1.3.1.regionlist.json)
for regionforbucket in $regionlist
do
	aws cloudformation create-stack --template-body file://./lab1.3.1.s3.yml --stack-name jmd-020201211-008 --region $regionforbucket
done
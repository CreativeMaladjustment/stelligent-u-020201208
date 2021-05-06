from aws_cdk import (
    aws_iam as iam,
    aws_imagebuilder as imagebuilder,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    core
)

from datetime import datetime

class AwsImageBuilderPocStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        poc_component = imagebuilder.CfnComponent(self, "poc_component", name="poc_component", platform="Linux", version="1.0.0", )

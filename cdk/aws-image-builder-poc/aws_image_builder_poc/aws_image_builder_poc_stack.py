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

        poc_component = imagebuilder.CfnComponent(self, "poc_component", name="pocYumU", platform="Linux", version="1.0.0", 
        data="yum update -y")
        
                
        # ami_distro_config = {
        #     "name": "pocYumU - {{ imagebuilder:buildDate }}",
        #     "Description": "WIP: yum update for proof of concept imagebuilder pipeline"
        # }
        
        ami_distro_property = iamgebuilder.CfnDistributionConfiguration.DistributionProperty(
            region=self.region,
            ami_distribution_configuration=[{"name": "pocYumU - {{ imagebuilder:buildDate }}","Description": "WIP: yum update for proof of concept imagebuilder pipeline"}]
        )

        image_recipe = imagebuilder.CfnImageRecipe(self, "pocRecipe", name ="pocYumU", version="0.0.1",
            components=[{"componentArn": poc_component.attr_arn}]
            parent_image=f"arn:{data['aws_partition']['current']['partition']}:imagebuilder:{data['aws_region']['current']['name']}:aws:image/amazon-linux-2-x86/x.x.x",
        )

        infra_config = imagebuilder.CfnInfrastructureConfiguration(self, "pocInfraConfig", name="pocYumU", instance_types=["t3.medium"], 
            instance_profilename="", ### need an instance profilename
            subnet_id="",            ### need the subnets
            security_group_ids=[""], ### need the sgs
            terminate_instance_on_failure=False
        )
        
        #need pipeline next
        #and scheduleproperty
        
        
        
        
from aws_cdk import core as cdk
from aws_cdk import aws_codecommit as codecommit

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class SiC020210618CodeCommitStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sic020210618 = codecommit.Repository(self, "sic020210618", repository_name="sic020210618" description="spot to place cdk code to execute with a pipeline")

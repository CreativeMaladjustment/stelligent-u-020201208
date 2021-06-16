#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from sic_020210618.sic_020210618_stack import SiC020210618Stack
from sic_020210618.sic_020210618_codecommit_stack import SiC020210618CodeCommitStack
from sic_020210618.cloud9_stack import Cloud9Stack

app = core.App()
SiC020210618Stack(app, "SiC020210618Stack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=core.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

codecommit = SiC020210618CodeCommitStack(app, "sic-020210618-codecommit-stack")
cloud9_stack = Cloud9Stack(app, "sic020210618Cloud9")

app.synth()

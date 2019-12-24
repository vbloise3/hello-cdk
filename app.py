#!/usr/bin/env python3

from aws_cdk import core

from hello_cdk.hello_cdk_stack import HelloCdkStack


app = core.App()
HelloCdkStack(app, "HelloCdkStack", env=core.Environment(region="us-east-1", account="001178231653"))

app.synth()

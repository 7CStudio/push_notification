# -*- coding: utf-8 -*-

import json
import boto


class AwsSNS(object):

    def __init__(
            self, aws_access_key_id, aws_secret_access_key,
            aws_sns_region, aws_android_arn):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_sns_region = aws_sns_region
        self.aws_android_arn = aws_android_arn

    def register_device(self, device):
        attributes = {'Enabled': True}
        custom_user_data = {"user_id": device.user_id, "device_id": device.id}

        boto.connect_sns(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)

        sns_conn = boto.sns.connect_to_region(
            region_name=self.aws_sns_region,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)

        response = sns_conn.create_platform_endpoint(
            token=device.token, platform_application_arn=self.aws_android_arn,
            custom_user_data=custom_user_data, attributes=attributes)
        response_key = 'CreatePlatformEndpointResponse'
        result_key = 'CreatePlatformEndpointResult'
        arn = response[response_key][result_key]['EndpointArn']
        return arn

    def send_notification_to_device(self, device, message, message_format):
        payload = json.dumps({"GCM": json.dumps({"data": message})})

        boto.connect_sns(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)

        sns_conn = boto.sns.connect_to_region(
            region_name=self.aws_sns_region,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)
        sns_conn.publish(
            target_arn=device.aws_sns_arn,
            message=payload,
            message_structure=message_format)

# -*- coding: utf-8 -*-

from django.conf import settings


class ServiceType(object):
    AWS_SNS = 'sns'


class AwsSNS(object):

    def __init__(
            self, aws_access_key_id=None, aws_secret_access_key=None,
            aws_sns_region=None, aws_android_arn=None):
        pass


class PushNotification(object):

    def __init__(
            self, service_type,
            aws_access_key_id=None, aws_secret_access_key=None,
            aws_sns_region=None, aws_android_arn=None):

        if service_type == ServiceType.AWS_SNS:
            self.notification_service = AwsSNS(
                aws_access_key_id=aws_access_key_id or settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=aws_secret_access_key or settings.AWS_SECRET_ACCESS_KEY,
                aws_sns_region=aws_sns_region or settings.AWS_SNS_REGION,
                aws_android_arn=settings.AWS_ANDROID_ARN)

    def register_device(self, user, device, platform):
        pass

    def dispatch_notification(self, user, message):
        pass

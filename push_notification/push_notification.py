# -*- coding: utf-8 -*-

from django.conf import settings

from .aws_sns import AwsSNS
from .models import Device


class ServiceType(object):
    AWS_SNS = 'sns'


class DevicePlatform(object):
    ANDROID = 'android'


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

    def register_device(self, user, device_token, device_platform):
        device, created = Device.objects.get_or_create(
            user=user, token=device_token, platform=device_platform)
        arn = self.notification_service.register_device(device)
        device.aws_sns_arn = arn
        device.save()

    def dispatch_user_notification(self, user, message, message_format='json'):
        for device in user.device_set.all():
            message['device_token'] = device.token or ""
            self.notification_service.send_notification_to_device(
                device, message, message_format)

    def remove_device(self, user, device_token, device_platform):
        device = Device.objects.get(
            user=user, token=device_token, platform=device_platform)
        self.notification_service.remove_device(device)
        device.delete()

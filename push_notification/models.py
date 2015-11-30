# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=255)
    aws_sns_arn = models.CharField(max_length=255, null=True)
    platform = models.CharField(max_length=10)

    class Meta:
        app_label = 'push_notification'

    def __unicode__(self):
        return u"{} {} {}".format(self.user, self.token, self.platform)

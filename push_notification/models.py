# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=255, unique=True)
    aws_sns_arn = models.CharField(max_length=255, null=True)
    platform = models.CharField(max_length=10)

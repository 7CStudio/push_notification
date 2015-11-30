#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='push_notification',
    version='0.0.5',
    packages=['push_notification'],
    license='MIT',
    install_requires=[
        # -*- Extra requirements: -*-
        'boto==2.38.0',
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import Theatre_CS399
version = Theatre_CS399.__version__

setup(
    name='Theatre',
    version=version,
    author='',
    author_email='kyle.a.mcginn@gmail.com',
    packages=[
        'Theatre_CS399',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['Theatre_CS399/manage.py'],
)

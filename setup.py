#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import booktracker
version = booktracker.__version__

setup(
    name='BookTracker',
    version=version,
    author='',
    author_email='robert.thornton@gmail.com',
    packages=[
        'booktracker',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['booktracker/manage.py'],
)

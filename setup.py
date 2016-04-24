#! /usr/bin/env python

import dedrm

from setuptools import setup, find_packages

packages = [
    'dedrm',
]

setup(
    name='dedrm',
    version=dedrm.PLUGIN_VERSION,
    description='Apprentice Alf\'s DRM Tools',
    long_description='Apprentice Alf\'s DRM Tools',
    author='',
    author_email='',
    url='',
    packages=find_packages(),
)

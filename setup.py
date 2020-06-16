#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages


VERSION = '0.0.0'
LONGDESC = '''
Cidr-Runner
===========

A tool to compile network configurations across an AWS Organization.
'''


setup(
    name='cidr-runner',
    version=VERSION,
    description='A tool to compile network configurations across an AWS Organization.',
    long_description=LONGDESC,
    long_description_content_type='text/x-rst',
    url='https://github.com/weednix/cidr-runner',
    project_urls={
        'Issues': 'https://github.com/weednix/cidr-runner/issues',
    },

    keywords='aws network organizations boto3 ',
    author='Ashley Gould - weednix',
    author_email='agould@ucop.edu',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'botocore',
        'boto3',
        'PyYAML',
        'click',
        'orgcrawler',
    ],
    packages=find_namespace_packages(
        include=['cidr_runner'],
    ),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'cidrrunner=cidr_runner.cli:main',
        ],
    },
)

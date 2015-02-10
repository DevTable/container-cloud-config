#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='container-cloud-config',
    version='0.0.1',
    author="Jake Moshenko",
    author_email="jake.moshenko+pip@coreos.com",
    description="Module for helping to create cloud config for running containers",
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={'': ['templates/*.yaml']},
    include_package_data=True,
    install_requires=['requests', 'jinja2'],
    url='http://github.com/devtable/container-cloud-config',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    license="Apache",
)
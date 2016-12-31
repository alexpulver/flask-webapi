#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='Flask web API skeleton',
    version='0.1.0',
    author='Alex Pulver',
    author_email='alex.pulver@gmail.com',
    py_modules=['run'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=['Flask', 'Flask-RESTful', 'gunicorn'],
    tests_require=['coverage', 'mock'],
    test_suite='tests',
)

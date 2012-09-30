#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

setup(
  name='m2tool',
  version='0.1',
  url="https://github.com/daltonmatos/m2tool",
  license="3-BSD",
  description='m2tool is a command line tool to manage mongrel2 instances',
  author="Dalton Barreto",
  author_email="daltonmatos@gmail.com",
  long_description=open(os.path.join(ROOT, 'README.rst')).read(),
  packages=['m2tool'],
    entry_points={
        'console_scripts': [
            'm2tool = m2tool.main:main',
            ]
    },
  install_requires = ['python-modargs'],
  classifiers = [
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Application Frameworks"
    ])


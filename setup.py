#!/usr/bin/env python
from setuptools import setup

setup(name='scp.py',
      version='0.1',
      description='SCP module for paramiko',
      author=u'JBardin',
      author_email='',
      url='http://github.com/kapliars/scp.py',
      packages=['scp'],
      requires=['paramiko'],
      entry_points = {}
)

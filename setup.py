#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup
import os.path as p

VERSION = open(p.join(p.dirname(p.abspath(__file__)), 'VERSION')).read().strip()

setup(
    name='jsonpipe',
    version=VERSION,
    description="Convert JSON to a UNIX-friendly line-based format.",
    author='Zachary Voase',
    author_email='z@dvxhouse.com',
    url='http://github.com/dvxhouse/jsonpipe',
    package_dir={'': 'src'},
    py_modules=['jsonpipe'],
    entry_points={'console_scripts': ['jsonpipe = jsonpipe:main']},
    install_requires=['simplejson>=2.1.3'],
    test_suite='jsonpipe._get_tests',
)

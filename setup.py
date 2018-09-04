#!/usr/bin/env python
# Copyright 2018 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Python 101 Slides
We're using setup here because it makes it easy to change Python versions

Requires: Sphinx, hieroglyph

Commands:
    python3 setup.py spelling
    python3 setup.py html
    python3 setup.py slides
"""

from setuptools import setup

setup(
    name='python101',
    version='1.0.0',
    description='Python 101 Slides',
    long_description='Python 101 Slides',
    author='Avram Lubkin',
    author_email='avylove@rockhopper.net',
    maintainer='Avram Lubkin',
    maintainer_email='avylove@rockhopper.net',
    url='https://github.com/avylove/python101',
    license='MPLv2.0',
    zip_safe=False,
    install_requires=['Sphinx', 'hieroglyph'],
)

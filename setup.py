# -*- coding: utf-8 -*-

# Copyright 2016 shipa authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from setuptools import setup, find_packages

setup(
    name="shipa-sphinx",
    url="https://github.com/shipa-c/shipa-sphinx",
    version='0.1.4',
    description="Sphinx extensions used in shipa documentation",
    author="Shipa",
    author_email="shipa@corp.globo.com",
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=[
        "docutils==0.12",
        "PyYAML==3.11",
    ],
    entry_points={
        'console_scripts': [
            'shipa_sphinx=shipa_sphinx:main',
        ],
    },
)

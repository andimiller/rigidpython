# encoding: utf-8

from setuptools import setup
import os.path

setup(
    name="rigidpython",
    version="0.0.1",
    author="andimiller",
    author_email="andi at andimiller dot net",
    maintainer="andimiller",
    maintainer_email="andi at andimiller dot net",
    description="Collection of tools for type enforcement in python",
    long_description = os.path.isfile("README.md") and open('README.md').read() or None,
    license=(
        "Copyright (C) 2014-Present Andi Miller"
        "All Rights Reserved. "
        "See LICENSE for the full license."
    ),
    url="https://github.com/andimiller/rigidpython",
    packages=['rigidpython'],
    install_requires=[
    	'six'
    ],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

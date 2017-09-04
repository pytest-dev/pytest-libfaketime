#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-libfaketime',
    version='0.1.0',
    author='Éloi Rivard',
    author_email='eloi@yaal.fr',
    maintainer='Éloi Rivard',
    maintainer_email='eloi@yaal.fr',
    license='MIT',
    url='https://github.com/azmeuk/pytest-libfaketime',
    description='A python-libfaketime plugin for pytest.',
    long_description=read('README.md'),
    py_modules=['pytest_libfaketime'],
    install_requires=[
        'libfaketime',
        'pytest>=3.1.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'libfaketime = pytest_libfaketime',
        ],
    },
)

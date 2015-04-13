#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pip.req import parse_requirements

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

requirements = [str(ir.req) for ir in install_reqs]
test_requirements = requirements


setup(
    name='vulyk_build',
    version='0.1.0',
    description="Build test project",
    long_description=readme + '\n\n' + history,
    author="Volodymyr Hotsyk",
    author_email='gotsyk@gmail.com',
    url='https://github.com/hotsyk/vulyk-build',
    packages=[
        'vulyk_build',
    ],
    package_dir={'vulyk_build':
                 'vulyk_build'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='vulyk-build',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

# Encoding: utf-8

# --
# Copyright (c) 2008-2019 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

import os

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as long_description:
    LONG_DESCRIPTION = long_description.read()

setup(
    name='nagare-server-cli',
    author='Net-ng',
    author_email='alain.poirier@net-ng.com',
    description='Nagare command line applications',
    long_description=LONG_DESCRIPTION,
    license='BSD',
    keywords='',
    url='https://github.com/nagareproject/server-cli',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=['nagare-commands', 'nagare-services', 'nagare-server'],
    tests_require=['pytest'],
    entry_points='''
        [nagare.services]
        exceptions = nagare.services.cli_exceptions_handler:Exceptions

        [nagare.applications]
        cli = nagare.server.cli_application:CLIApp

        [nagare.publishers]
        cli = nagare.server.cli_publisher:Publisher
    '''
)

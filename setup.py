#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

__version__ = '0.1.1'

setup(
    name='ssh_tunneler',
    version=__version__,
    long_description=long_description,
    description='Tool for setting up SSH tunnels.',
    url='http://www.github.com/rfaulkner/tunneler',
    author="Wikimedia Foundation",
    author_email="rfaulkner@wikimedia.org",
    scripts=['run_ssh_tunnels'],
    classifiers=[
        'Development Status :: 3 - Release',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    data_files=[('readme', ['README.md'])]
)

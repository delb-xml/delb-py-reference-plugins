
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='delb-reference-plugins',
    version='0.2b2',
    description="A package with spare non-sense plugins for delb as developer's reference.",
    python_requires='==3.*,>=3.6.0',
    author='Frank Sachsenheim',
    author_email='funkyfuture@riseup.net',
    license='AGPL-3.0',
    entry_points={"delb": ["custom-loader = delb_reference_plugins.custom_loader", "header-properties = delb_reference_plugins.header_properties"]},
    packages=['delb_reference_plugins'],
    package_dir={"": "."},
    package_data={},
    install_requires=['delb==0.2b2'],
)

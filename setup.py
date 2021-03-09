#!/usr/bin/env python3

# Note!
# ' are required, do not use any '.

# setup.
from setuptools import setup, find_packages
setup(
	name='dev0s',
	version='2.16.6',
	description='Some description.',
	url='http://github.com/vandenberghinc/dev0s',
	author='Daan van den Bergh',
	author_email='vandenberghinc.contact@gmail.com',
	license='MIT',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[
            'django',
            'requests',
            'pathlib',
            'pexpect',
        ])
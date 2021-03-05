#!/usr/bin/env python3

# Note!
# ' are required, do not use any '.

# setup.
from setuptools import setup, find_packages
setup(
	name='fil3s',
	version='2.13.0',
	description='Some description.',
	url='http://github.com/vandenberghinc/fil3s',
	author='Daan van den Bergh',
	author_email='vandenberghinc.contact@gmail.com',
	license='MIT',
	packages=find_packages(),
	zip_safe=False,
	install_requires=[
            'requests',
            'pathlib',
        ])
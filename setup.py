#name =!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='Siphon-Client',
    version='0.0.1',
    author='mitch',
    author_email='mitchfriedman@gmail.com',
    description='A basic siphon client',
    include_package_data=True,
    install_requires=[
        'clint', 'flake8',
    ],
    entry_points={
        'console_scripts': [
            'sc = client.client.run',
        ]
    }
)


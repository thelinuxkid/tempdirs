#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='tempdirs',
    version='0.0.4',
    description='tempdirs -- Safely create temporary directories',
    long_description=(
        'tempdirs is a library which allows users to safely and '
        'cleanly create any number of temporary directories. Temporary '
        'directories are automatically deleted. It was created as a '
        'testing utility.'
        ),
    author='Andres Buritica',
    author_email='andres@thelinuxkid.com',
    maintainer='Andres Buritica',
    maintainer_email='andres@thelinuxkid.com',
    url='https://github.com/thelinuxkid/tempdirs',
    packages = find_packages(),
    py_modules=['tempdirs'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ],
)

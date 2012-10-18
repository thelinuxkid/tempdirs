#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name='tempdirs',
    version='0.0.3',
    description='tempdirs -- Safely create temporary directories',
    long_description=(
        'tempdirs is a library which allows users to safely and '
        'cleanly create any number of temporary directories. Temporary '
        'directories are automatically deleted. It was created as a '
        'testing utility.'
        ),
    license='GPL',
    author='Andres Buritica',
    author_email='andres@thelinuxkid.com',
    maintainer='Andres Buritica',
    maintainer_email='andres@thelinuxkid.com',
    url='https://github.com/andresburitica/tempdirs',
    packages = find_packages(),
    py_modules=['tempdirs'],
)

#!/usr/bin/python
from setuptools import setup, find_packages

# Pypi package documentation
with open('README.rst') as fp:
    long_description = fp.read()

setup(
    name='tempdirs',
    version='0.0.5',
    description='tempdirs -- Safely create temporary directories',
    long_description=long_description,
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

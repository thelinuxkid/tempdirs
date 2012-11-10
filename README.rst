========
tempdirs
========

Description
===========

tempdirs is a library which allows users to safely and cleanly create
any number of temporary directories. Temporary directories are
automatically deleted. It was created as a testing utility.

Installation
============

Install using pip::

    pip install pyusps

or easy_install::

    easy_install pyusps

Examples
========

You can tempdirs.makedirs as a decorator passing in the number of
temporary directories needed::

    import os

    import tempdirs

    @tempdirs.makedirs(2)
    def test_foo(**kwargs):
        (srcdir, dstdir) = kwargs['tempdirs_dirs']
        srcfile = os.path.join(srcdir,'foo')
        dstfile = os.path.join(dstdir,'bar')
        with open(srcfile, 'w') as fp:
            fp.write('src content\n')
        with open(dstfile, 'w') as fp:
            fp.write('dst content\n')

You can also use tempdirs.makedirs as a Context Manager::

    import os

    import tempdirs

    with tempdirs.makedirs(2) as (srcdir, dstdir):
        srcfile = os.path.join(srcdir,'foo')
        dstfile = os.path.join(dstdir,'bar')
        with open(srcfile, 'w') as fp:
            fp.write('src content\n')
        with open(dstfile, 'w') as fp:
            fp.write('dst content\n')

Developing
==========

External dependencies
---------------------

    - python-dev
    - python-setuptools
    - python-virtualenv

Setup
-----

To start developing run the following commands from the project's base
directory. You can download the source from
https://github.com/thelinuxkid/tempdirs::

    # I like to install the virtual environment in a hidden repo.
    virtualenv .virtual
    # I leave the magic to Ruby developers (.virtual/bin/activate)
    .virtual/bin/python setup.py develop

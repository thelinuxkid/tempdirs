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

You can use pip or easy_install

- pip install tempdirs
- easy_install tempdirs

Examples
========

Use tempdirs as a decorator passing in the number of temporary
directories needed::

    import os

    import tempdirs

    @tempdirs.makedirs(2)
    def test_foo(srcdir, dstdir):
        srcfile = os.path.join(srcdir,'foo')
        dstfile = os.path.join(dstdir,'bar')
        with open(srcfile, 'w') as fp:
            fp.write('src content\n')
        with open(dstfile, 'w') as fp:
            fp.write('dst content\n')

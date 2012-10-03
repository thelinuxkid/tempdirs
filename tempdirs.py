import functools
import tempfile
import shutil

class makedirs(object):
    def __init__(self, num=1):
        self._num = num

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            def manager():
                try:
                    dirs = [
                        tempfile.mkdtemp()
                        for i in xrange(self._num)
                        ]
                    extra_args = list(args)
                    extra_args += dirs
                    fn(*extra_args, **kwargs)
                finally:
                    for dir_ in dirs:
                        try:
                            shutil.rmtree(dir_)
                        except OSError, e:
                            # It's OK if dir doesn't exist
                            if e.errno != 2:
                                raise

            return manager()
        return wrapper

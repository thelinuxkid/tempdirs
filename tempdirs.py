import sys
import functools
import tempfile
import shutil
import errno

NO_EXC = (None, None, None)

# Inspiration from http://code.google.com/p/contextdecorator
class DecoratorContext(object):
    def decorated_fn(self, fn, *args, **kwargs):
        return fn(*args, **kwargs)

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            exc = NO_EXC
            result = None
            try:
                self.__enter__()
                result = self.decorated_fn(fn, *args, **kwargs)
            except Exception:
                exc = sys.exc_info()
            finally:
                supress = self.__exit__(*exc)
                if not supress and exc is not NO_EXC:
                    (cls, val, tb) = exc
                    raise cls, val, tb
            return result
        return wrapper

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

class makedirs(DecoratorContext):
    def __init__(self, num=1):
        self._num = num

    def decorated_fn(self, fn, *args, **kwargs):
        extra_args = list(args)
        extra_args = self._dirs + extra_args
        return fn(*extra_args, **kwargs)

    def __enter__(self):
        self._dirs = [
            tempfile.mkdtemp()
            for i in xrange(self._num)
        ]
        return self._dirs

    def __exit__(self, *exc):
        for dir_ in self._dirs:
            try:
                shutil.rmtree(dir_)
            except OSError, e:
                # It's OK if dir doesn't exist
                if e.errno != errno.ENOENT:
                    raise
        return False

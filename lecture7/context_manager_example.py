# 1.
# Opened takes a path we need to open,
# and is a context manager for files
from functools import partial


class opened:
    def __init__(self, path, *args, **kwargs):
        self.opener = partial(open, path, *args, **kwargs)

    def __enter__(self):
        self.handle = self.opener()
        return self.handle

    def __exit__(self, *exc_info):
        self.handle.close()
        del self.handle
        # No need for return, since None is falsy value


with opened("example.txt", mode="rt") as handle:
    pass

# 2.
# TempFiles
import tempfile

with tempfile.TemporaryFile() as handle:
    path = handle.name
    print(path)

# open(path) ==> OSError: [Errno 9] Bad file descriptor

# 3.
# cd
# Saves current directory,
# __enter__ : changes it,
# __exit__ : changes back
import os


class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc_info):
        os.chdir(self.saved_cwd)


print(os.getcwd())
with cd("/tmp"):
    print(os.getcwd())

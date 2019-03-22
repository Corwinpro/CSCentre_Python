"""
Previously we discussed how to create different context managers.
One of the examples was cd, a context manager that changes the
current working directory and goes back on exit.
The implementation contained a lot of 'useless' things which can be
skipped if you use contextlib and create a generator for this 
context manager.
"""

import os


class cd:
    """
    Straightforward implementation of cd context manager
    """

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, *exc_info):
        os.chdir(self.saved_cwd)


"""
There's a special decorator for this!
"""
from contextlib import contextmanager


@contextmanager
def cd2(path):  # __init__
    old_cwd = os.getcwd()  # __enter__
    os.chdir(path)  # We change directory here
    try:
        yield  # and give the control to 'with' here
    finally:  # We need try - finally here because if we get an Exception we still want to go to old_cwd
        os.chdir(old_cwd)  # __exit__ <- we always want to execute this


"""
Same applies to a tmp file
"""
import tempfile
import shutil


@contextmanager
def tempdir():
    outdir = tempfile.mkdtemp()
    try:
        yield outdir  # outdir goes to 'as ...'
    finally:
        shutil.rmtree(outdir)


with tempdir() as path:
    print(path)

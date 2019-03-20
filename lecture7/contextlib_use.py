# 1.
# closing extends 'open' logic to any class with close() method
from contextlib import closing
from urllib.request import urlopen

url = "http://compscicenter.ru"
with closing(urlopen(url)) as page:
    # Do something with webpage
    # and then close it
    pass

# 2.
# redirect stdout
# We could implement redirect_stdout as:
# - in __enter__ : sys.stdout = handle
# in __exit__ : return it back
from contextlib import redirect_stdout
import io

handle = io.StringIO()
with redirect_stdout(handle):
    print("Hello, World!")

print(handle.getvalue())

# 3.
# 'suppress' suppresses exceptions
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("example.txt")

# This is how it works:
class my_suppress:
    def __init__(self, *suppressed):
        self.suppressed = suppressed

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, tb):
        return exc_type is not None and issubclass(exc_type, self.suppressed)


# 4.
# ContextDecorator
from contextlib import suppress as _suppress, ContextDecorator


class suppressed(_suppress, ContextDecorator):
    pass


@suppressed(TypeError)
def do_smth():
    a = 1 + "42"


do_smth()

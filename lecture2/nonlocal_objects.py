# Nonlocal objects
def cell(value=None):
    def get():
        return value

    def set(update):
        nonlocal value
        value = update

    return get, set


get, set = cell()
print(get())
set(42)
print(get())

# How should we store data in descriptors?

# 1.
# In descriptor itself
class Proxy:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class A:
    attr = Proxy()


a = A()
a.attr = 42
other_a = A()
other_a.attr  # 42 ???

# The problem here is that descriptor is one for class,
# and all attributes share it

# 2.
# Store in dict for each instance
class Proxy_wDict:
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance not in self.data:
            raise AttributeError
        return self.data[instance]

    def __set__(self, instance, value):
        self.data[instance] = value


# Instance should be hashable
# Another problem is: memory leak. All the instances ever created with Proxy_wDict will be there.

# 3.
# Explicitly in class instance
class Proxy_inInstance:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        return instance.__dict__[self.label]

    def __set__(self, instance, value):
        instance.__dict__[self.label] = value


class B:
    attr = Proxy_inInstance("attr")


b = B()
b.attr = 42
b.attr  # 42

# 4.
# Welcome to 3.6.+


class Proxy_wName:
    def __get__(self, instance, owner):
        if instance.__dict__[self.name] == 42:
            print("Hooray!")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class C:
    attr = Proxy_wName()


c = C()
c.attr = 42
c.attr  # 42


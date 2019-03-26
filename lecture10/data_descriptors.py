# 1.
# We can split descriptors into two groups:
# Data descriptors: at least define __set__ method
# Non-data descriptors: the rest
# The difference is how the interact with __dict__ of a class instance

# 2.
# Data descriptor
# Accessing an attribute attr is forwarded to the method DataDescr.__get__ if:
# DataDescr is a Data Descriptor with __get__ (and __set__ since it's a data descriptor)
class DataDescr:
    def __get__(self, instance, owner):
        print("DataDescr.__get__")

    def __set__(self, instance, value):
        print("DataDescr.__set__")


class A:
    attr = DataDescr()


instance = A()
# __get__ is called because a) attr is data descriptor, and it has __get__
instance.attr  # ==> DataDescr.__get__
# We can hack the attribute with __dict__:
instance.__dict__["attr"] = 42
# But this still call __get__
instance.attr  # ==> DataDescr.__get__


# 3. Non-data descriptor
# Accessing an attribute attr is forwarded to __get__ only if there's no such attribute in instance.__dict__
class NonDataDescr:
    def __get__(self, instance, owner):
        print("NonDataDescr.__get__")


class B:
    attr = NonDataDescr()


instance = B()
instance.attr  # ==> NonDataDescr.__get__
instance.__dict__["attr"] = 42
# Now the instance has 'attr' in dict, so __get__ is no longer called
instance.attr  # ==> 42


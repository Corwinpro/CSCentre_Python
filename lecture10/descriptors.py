# 1.
# We discussed @property previously, which are some attributes that are computed dynamically
# Descriptors semantics:
# Let:
#   instance - instance of class cls
#   attr - descriptor attribute of cls
#   descr = cls.__dict__["attr"] - the descriptor itself
# Then:
#   cls.attr == descr.__get__(None, cls)
#   instance.attr ~= descr.__get(instance, cls)
#   instance.attr = value == descr.__set__(instance, value)
#   del instance.attr == descr.__delete__(instance)
# An example:


class VerySafe:
    def __get_attr(self):
        return self.x

    def _set_attr(self, x):
        assert x > 0, "non-negative value required"
        self._x = x

    def _del_attr(self):
        del self._x

    x = property(__get_attr, _set_attr, _del_attr)


# What is we want a new attribute 'y' which is also safe?
# Descriptor is a 'property' which we can use multiple times
# it know how to get, set and delete this attribute


class NonNegative:
    def __get__(self, instance, owner):
        # instance = class instance (or None, if the descriptor was called when by class attribute)
        # owner = class, that 'owns' the descriptor
        pass

    def __set__(self, instance, value):
        pass

    def __del__(self, instance):
        pass


# now we can reuse this property


class VerySafe_with_descriptor:
    x = NonNegative()
    y = NonNegative()


# 2.
# Now let's see how __get__ works:
class Descr_get:
    def __get__(self, instance, owner):
        print(instance, owner)


class A:
    attr = Descr_get()


A.attr  # ==> None <class '__main__.A> - instance is None, since we call by class attribute, and owner is class A
A().attr  # <__main__.A object at [...]> <class '__main__.A> now instance is not None but a specific instance

# This is what happens when we inheret:
class B(A):
    pass


B.attr  # ==> None <class '__main__.B>
B().attr  # <__main__.B object at [...]> <class '__main__.B>

# 3.
# Now let's see how __set__ works:
class Descr_set:
    def __set__(self, instance, value):
        print(instance, value)


class C:
    attr = Descr_set()


instance = C()
instance.attr = 42  # ==> <__main__.C object at [...]> 42
# this line will just rewrite the attribute attr of class C, so no descriptor in class C anymore
# descriptor only works with class instances
C.attr = 42


# 4.
# Delete only needs instance
# It is called __delete__ because __del__ is a class desctructor


class Descr_del:
    def __delete__(self, instance):
        print(instance)


class D:
    attr = Descr_del()


del D().x  # ==> <__main__.D object at [...]>
del D.x  #

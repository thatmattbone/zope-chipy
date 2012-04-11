"""
Diff two identical classes, one that implements a zope interface and
one that does not to examine the metadata that is added.
"""

from zope.interface import Interface, implementer
import pprint

class IFoo(Interface):
    def some_method():
        """This is a method that implementers are supposed to
        implement."""


@implementer(IFoo)
class FooImplementsInterface():
    def some_method():
        pass


class FooDoesNotImplementInterface():
    def some_method():
        pass


if __name__ == "__main__":
    foo_implements = FooImplementsInterface()
    foo_does_not_implement = FooDoesNotImplementInterface()

    diffs = []
    for attr in dir(foo_implements):
        if attr not in dir(foo_does_not_implement):
            diffs.append(attr)

    pprint.pprint(diffs)

import zope.interface
import zope.interface.verify


def ascending_invariant(ascending_list):
    prev = None
    for item in ascending_list:
        if prev is None:
            prev = item
        elif prev > item:
            raise zope.interface.Invalid


class IAscendingList(zope.interface.Interface):
    zope.interface.invariant(ascending_invariant)


@zope.interface.implementer(IAscendingList)
class AscendingList(list):
    pass


@zope.interface.implementer(IAscendingList)
class StubList(object):
    pass


if __name__ == "__main__":

    #zope.interface.classImplements(AscendingList, IAscendingList)
    zope.interface.verify.verifyObject(IAscendingList, StubList())
    
    #my_list = AscendingList()
    #my_list.extend([1, 2, 3])
    #print(my_list)

    #IAscendingList.validateInvariants(my_list)
    #zope.interface.verify.verifyObject(IAscendingList, my_list)


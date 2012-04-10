from zope.interface import implementer, invariant, Invalid, Interface
from zope.interface.verify import verifyObject


def ascending_invariant(ascending_list):
    """
    Make sure the list is in ascending order. 

    Raise a zope.interface.Invalid exception if it is not.
    """
    if len(ascending_list) > 0:
        prev = ascending_list[0]
        for item in ascending_list:
            if prev > item:
                raise Invalid


class IAscendingList(Interface):
    invariant(ascending_invariant)


@implementer(IAscendingList)
class AscendingList(list):
    pass


def verify_ascending_list():
    verifyObject(IAscendingList, AscendingList([1, 2, 3]))


def verify_nonascending_list():
    """
    verifyObject() does not check invariants, so this verification
    will pass even though this list is not ascending.
    """
    verifyObject(IAscendingList, AscendingList([3, 2, 1]))


def validate_ascending_list():
    IAscendingList.validateInvariants(AscendingList([1, 2, 3]))


def validate_nonascending_list():
    IAscendingList.validateInvariants(AscendingList([3, 2, 1]))


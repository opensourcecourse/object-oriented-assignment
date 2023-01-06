"""
Second task of OO project.

Simply fill in some implementation details to learn about other important
OO features.
"""


class HelicopterParent:
    """A class which keeps a registry of all its sub-classes."""

    children = []

    # implement logic here to append the class object of each subclass
    # to the children list.


class Getter:
    """A class with a dynamic property."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # implement property C to be equal to a + b (even when a or b changes)


class Setter:
    """A class with dynamic attribute setting behavior."""

    def __init__(self, a):
        self.old_values_of_a = []
        ...

    # implement a setter which appends the old values of a to the list
    # 'old_values_of_a' each time a new value is set.


class RichParent:
    """A parent."""

    asset_1 = 10_000
    asset_2 = 200_000
    asset_3 = 600_000

    # Implement a method called "get_net_worth" which adds up all asset values
    # this should work even if new assets are added (e.g., asset_4 or
    # asset_1022)


class ChildMoocher(RichParent):
    """A child class that inherits too much."""

    siblings = 3

    # Implement a method also called "get_net_worth" which calls the parent's
    # get_net_worth function then returns the result divided by siblings.

"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False
"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""

        # check if left is less than root and right is greater than root
        # pre order traversal
        # while a tree
            # if left.data less than root
                # is_valid = True
                # run is_valid to node.left
            # root
            # if right.data is great than the root
                # is_valid = True
                # run is_valid to node.right
            # else
                #is_valid = False
                #break

        curr = self

        if curr != None:

            print('got to here')

            if curr.left.data < curr.data:
                valid = True
                print('valid ===>', valid)
                is_valid(curr.left)

            if curr.right.data < curr.data:
                valid = True
                is_valid(curr.right)

            else:
                valid = False

        return valid


t = Node(4,Node(2, Node(1), Node(3)),Node(6, Node(1), Node(7)))
print(t.is_valid())

# if __name__ == "__main__":
#     import doctest

#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASSED; THAT'S VALID!\n")


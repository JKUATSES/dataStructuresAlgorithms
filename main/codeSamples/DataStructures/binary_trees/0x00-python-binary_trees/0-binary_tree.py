#!/usr/bin/python3
"""0-binary_tree module defines classes for creating
and interacting with a binary tree
"""


class Node:
    """ Class Node defines the structure of a single node of a binary tree

    Attributes:
        __data: Int value held by the node
        __left: Pointer to the left child of a parent/root
        __right: Pointer to the right child of parent/root

    """
    def __init__(self, data=None, left=None, right=None):
        """This method initializes a single node.

        Args:
            left (Node): This is a pointer to the left child of a parent/root

            data (Any): This defines the data that the node holds

            right (Node): This is a pointer to the right child of a parent/root

        """

        if type(data) is not int:
            raise TypeError("Data must be an integer value")

        elif (not isinstance(left, Node) and left is not None):
            raise TypeError("left must be an instance of Node")

        elif (not isinstance(right, Node) and right is not None):
            raise TypeError("right  must be an instance of Node")

        else:
            self.__left = left
            self.__data = data
            self.__right = right

    @property
    def left(self):
        """This method returns the left child of parent/root."""
        return (self.__left)

    @left.setter
    def left(self, left=None):
        """This method sets left child of parent/root.

        Args:
            left (Node): This is a pointer to the left child
            of a parent/root

        Raises:
            TypeError: When arguement is not of type Node

        """
        if (not isinstance(left, Node) and left is not None):
            raise TypeError("left must be an instance of Node")

        self.__left = left

    @property
    def data(self):
        """This method returns the data held by the node"""
        return (self.__data)

    @data.setter
    def data(self, data=None):
        """This method sets the data of the node.

        Args:
            data (int): This holds the data of the node.

        Raises:
            TypeError: When argument is not of type int

        """
        if type(data) is not int:
            raise TypeError("Data must be an integer value")

        self.__data = data

    @property
    def right(self):
        """This method returns the right child of parent/root."""
        return (self.__right)

    @right.setter
    def right(self, right=None):
        """This method sets right child of parent/root.

        Args:
            right_pointer (Node): This is a pointer to the right child
            of a parent/root

        Raises:
            TypeError: When arguement is not of type Node
        """

        if (not isinstance(right, Node) and right is not None):
            raise TypeError("right must be an instance of Node")

        self.__right = right



class BinaryTree:
    """ Class BinaryTree provides methods for creating, manipulating
    and traversing a binary tree.

    This class has no public class attributes

    """
    def __init__(self):
        """ This method initializes a single node """
        self.root = None

    def add(self, data):
        """This method creates the root of the binary tree if the root is None.
        Otherwise, it calls the _add() method
        and supplies it with the required arguement

        Args:
            data (Int): An integer value

        """
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """ This method adds a node to the the binary tree.
        Args:
            data (Int): An integer value
            node (Node): A node in the tree
        """
        if(data < node.data):
            if(node.left != None):
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if(node.right != None):
                self._add(data, node.right)
            else:
                node.right =  Node(data)

    def delete_binary_tree(self):
        """ This method deletes a binary tree """
        self.root = None

    def is_empty(self):
        """ This method checks whether the binary tree is empty"""
        return (self.root == None)

    def print_tree(self):
        """ This method prints calls the _print_tree() method
        if the root of the tree is not None
        """
        if(self.root != None):
            self._print_tree(self.root)
        else:
            print("The binary tree is empty")

    def _print_tree(self, node):
        """ This method recursively prints the values of the nodes in the tree

        Args:
            node (Node): A node in the tree

        """
        if (node != None):
            self._print_tree(node.left)
            print("{:d} is a value held in a node".format(node.data))
            self._print_tree(node.right)

    def find(self, data):
        """ This calls the _find() method if the tree is not empty

        Args:
            data (Int): Integer value

        """
        if type(data) is not int:
            raise TypeError("Data must be an integer value")

        if(self.root != None):
            self._find(data, self.root)
        else:
            print("Found None")

    def _find(self, data, node):
        """ This method recursively searches the tree for the arguement supplied

        Args:
            data (Int): Integer value
            node (Node): A node in the tree

        """
        if (data == node.data):
            print("Found {:d} in {}".format(node.data, node))
        elif (data < node.data and node.left != None):
            self._find(data, node.left)
        elif (data > node.data and node.right != None):
            self._find(data, node.right)


def main():
    binary_tree = BinaryTree()
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(3)
    binary_tree.add(7)
    binary_tree.add(13)
    binary_tree.add(10)
    binary_tree.add(2)
    binary_tree.add(9)

    binary_tree.print_tree()

    binary_tree.find(10)

if __name__ == '__main__':
    main()

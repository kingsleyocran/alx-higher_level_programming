#!/usr/bin/python3
""" Module Singly List"""


class Node:
    """Node of a singly linked list.
    - Private instance attribute: data:
        - property def data(self)
        - property setter def data(self, value)
    - Private instance attribute: next_node:
        - property def next_node(self)
        - property setter def next_node(self, value)
    - Instantiation with data and next_node.
    Attributes:
        data (int): the data stored in the node
        next_node (Node): a pointer to the next node
            in the linked list
    """

    def __init__(self, data, next_node=None):
        """Initialize method
        Args:
            data (int): the data stored in the node.
            next_node (Node): a pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter of the attribute data
        Returns:
            data: the stored data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter of the attribure data
        Args:
            value (int): the given data
        Raises:
            TypeError: if value is not integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter of the next_node
        Returns:
            next_node: a pointer to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter of the next_node
        Args:
            value (Node): a pointer to the next node
        Raises:
            TypeError: if value not node or None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list.
    - Private instance attribute: head.
    - Simple instantiation.
    - Public instance method: def sorted_insert(self, value).
    Attributes:
        head (Node): a pointer to the singly linked list
    """

    def __init__(self):
        """
        Class initializer
        """
        self.head = None

    def __str__(self):
        """For the print statement in the main file."""
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list.
        Args:
            value (Node): node value to be inserted
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            new_node = Node(value)
            tmp = self.__head
            while tmp is not None:
                if tmp.__next_node is None:
                    tmp.__next_node = new_node
                    new_node.__next_node = None
                if new_node.__data < tmp.__next_node.__data:
                    new_node.__next_node = tmp.__next_node
                    tmp.__next_node = new_node
                tmp = tmp.__next_node

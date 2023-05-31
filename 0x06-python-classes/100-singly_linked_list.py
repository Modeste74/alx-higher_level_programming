#!/usr/bin/python3
""" defines classes for a singly linked list"""


class Node:
     """
     Node class represents a node of a singly linked list.
     
     Attributes:
        data (int): The data stored in the node.
        next_node (Node): Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initializes the a new node"""
        self.data = data
        self.next_node = node

    @property
    def data(self):
        """
        Get the data stored in the node.
        Returns:
            int: The data stored in the node.
        """
        return self.__data
    
    @data.setter
    def data(self, value):
        """
        Set the data of the node.
        Args:
            value (int): The value to be set as the data.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

        @property
        def next_node(self):
            """
            Get the reference to the next node.
            Returns:
                Node: The reference to the next node.
            """
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """
            Set the next node reference.
            Args:
                value (Node): The next node in the list.
            Raises:
                TypeError: If value is not a Node object.
            """
            if value is not None and not isinstance(value, Node):
                raise TypeError('next_node must be a Node object')
            self.__next_node = value

class SinglyLinkedList:
    """ the class reps singly linked list """
    
    def __init__(self):
        """Initialzes a new instance """

        self.head = None
    
    def __str__(self):
        """
        Returns string rep
        Return:
            str: string rep
        """
        node = self.head
        result = ""
        while node:
            result += str(node.data) + "\n"
            node = node.next_node
        return result

    def sorted_insert(self, value):
        """
        Inserts a new node
        Args:
            value (int): value to be inserted
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

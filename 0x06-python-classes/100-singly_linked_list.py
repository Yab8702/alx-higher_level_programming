#!/usr/bin/python3
''' A Modules for A Singly Linked List'''


class Node:
    ''' define a node for singly linked list'''

    def __init__(self, data, next_node=None):
        ''' Intializing the Node Class
        Args:
            data: the data of the singly llinkedlist
            next_node: the pointer of the next node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' Define A singly LinkedList '''

    def __init__(self):
        ''' Intializing the head pointer'''
        self.__head = None

    def sorted_insert(self, value):
        ''' insert a new node into the correct sorted position'''
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the print representation"""
        values = ""
        tmp = self.__head
        while tmp:
            values += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return values[:-1]

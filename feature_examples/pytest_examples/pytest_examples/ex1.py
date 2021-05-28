#!/usr/bin/env python3
#


class Node(object):
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        print(f" [ {self.data} ]->")

    def __repr__(self):
        print(f" [ {self.data} {self.nxt}]->")


class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insert(self,node):
        self.head = node
        self.next = node

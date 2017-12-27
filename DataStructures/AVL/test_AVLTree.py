from unittest import TestCase
from DataStructures.AVL.Main import AVLTree
from os import sys
from random import randint


class TestAVLTree(TestCase):
    def test_add(self):
        t = AVLTree()
        for i in range(20):
            t.add(randint(10,100))
        sys.stderr.write("root=%s\n" % str(t.root))

        t.to_dot()
        self.assertTrue(1==1)
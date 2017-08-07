from unittest import TestCase
from LinkedLists import SingleLinkedList


class TestSinglyLinkedList(TestCase):
    def test_append(self):
        from LinkedLists import SingleLinkedList

        # SingleLinkedList.SinglyLinkedList.prepend(SingleLinkedList.__class__,data=1)
        sll = SingleLinkedList.SinglyLinkedList()
        sll.prepend(1)
        sll.prepend(2)
        sll.prepend(3)
        sll.prepend(4)

        print(sll)
        self.assertMultiLineEqual(str(sll), '[4, 3, 2, 1]')


class TestSinglyLinkedList(TestCase):
    def test_find(self):
        from LinkedLists import SingleLinkedList
        sll = SingleLinkedList.SinglyLinkedList()
        for i in range(1,5):
            sll.prepend(i)

        print(sll)
        print(sll.find(2))

        # self.assertEqual(sll.find(2),2)
        # self.asse

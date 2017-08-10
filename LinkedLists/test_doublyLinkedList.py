from unittest import TestCase


class TestDoublyLinkedList(TestCase):
    def test_prepend(self):
        from LinkedLists.DoublyLinkedList import DoublyLinkedList
        dll = DoublyLinkedList()
        dll.prepend(1)
        dll.prepend(2)
        dll.prepend(3)
        dll.prepend(4)
        dll.prepend(5)
        print(dll)
        a = str(dll)
        b = '[5, 4, 3, 2, 1]'
        self.assertMultiLineEqual(a, b)


class TestDoublyLinkedList(TestCase):
    def test_reverse(self):
        from LinkedLists.DoublyLinkedList import DoublyLinkedList
        dll = DoublyLinkedList()
        for i in range(1,11):
            dll.prepend(i)

        print(dll)
        a = str(dll)
        dll.reverse()
        print(dll)
        b = str(dll)
        dll.reverse()
        c = str(dll)
        print(a,b,c)
        self.assertMultiLineEqual(a,c)

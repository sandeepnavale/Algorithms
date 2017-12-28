from unittest import TestCase
from random import randint


class TestSinglyLinkedList(TestCase):
    def test_append(self):
        from DataStructures.LinkedLists import SingleLinkedList

        # SingleLinkedList.SinglyLinkedList.prepend(SingleLinkedList.__class__,data=1)
        sll = SingleLinkedList.SinglyLinkedList()
        sll.prepend(1)
        sll.prepend(2)
        sll.prepend(3)
        sll.prepend(4)

        print(sll)
        self.assertMultiLineEqual(str(sll), '[4, 3, 2, 1]')

    def test_find(self):
        from DataStructures.LinkedLists import SingleLinkedList
        sll = SingleLinkedList.SinglyLinkedList()
        sll.prepend(1)
        sll.prepend(2)
        sll.prepend(3)
        sll.prepend(4)

        print(sll)
        node = sll.find(2)
        self.assertEqual(node.data,2)
        node = sll.find(4)
        self.assertEqual(node.data, 4)


    def test_reverse(self):
        from DataStructures.LinkedLists import SingleLinkedList
        sll = SingleLinkedList.SinglyLinkedList()
        ele = [randint(10, 100) for i in range(10)]
        for i in range(10):
            sll.append(ele[i])
        print("TEST REVERSE")
        print("Original Inputs",ele)
        print("Inputs in SLL", sll)
        sll.reverse()
        print('SLL After reversed',sll)
        ele.reverse()
        print('Input reversed',ele)
        # self.assertAlmostEqual(sll,ele)


if __name__ == '__main__':
    unittest.main()
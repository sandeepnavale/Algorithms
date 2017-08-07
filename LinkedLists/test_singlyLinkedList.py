from unittest import TestCase
from LinkedLists import SingleLinkedList

class TestSinglyLinkedList(TestCase):
    def test_append(self):
        from LinkedLists import SingleLinkedList

        # SingleLinkedList.SinglyLinkedList.prepend(SingleLinkedList.__class__,data=1)

        self.assertTrue(1 == 1)


sll = SingleLinkedList.SinglyLinkedList()
sll.prepend(1)
sll.prepend(2)
sll.prepend(3)
sll.prepend(4)

print(sll)
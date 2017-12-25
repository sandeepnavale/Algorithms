class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)



class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        self.sorted = []
        self.get_inorder(self.root)
        return str(self.sorted)

    def get_inorder(self, node):
        if node:
            self.get_inorder(node.left)
            self.sorted.append(str(node.value))
            self.get_inorder(node.right)

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value <= node.value:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(node.right, value)
            else:
                node.right = Node(value)



from random import randint

bst = BST()

for i in range(10):
    bst.add(randint(1, 100))
print (bst)
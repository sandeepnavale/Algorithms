from random import randint

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

    def get_preorder(self,node):
        if node:
            print(node.value)
            self.get_preorder(node.left)
            self.get_preorder(node.right)

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

    def height(self,node):
        l=r=0
        if node.left:
           l = self.height(node.left)
        if node.right:
           r = self.height(node.right)

        return 1+max(l,r)

    def isBST(self,node):
        return (self.isBSTUtil(node, 0, pow(10,4)))

    # Retusn true if the given tree is a BST and its values
    # >= min and <= max
    def isBSTUtil(self,node, mini, maxi):

        # An empty tree is BST
        if node is None:
            return True

        # False if this node violates min/max constraint
        if node.value < mini or node.value > maxi:
            return False

        # Otherwise check the subtrees recursively
        # tightening the min or max constraint
        return (self.isBSTUtil(node.left, mini, node.value - 1) and
                self.isBSTUtil(node.right, node.value + 1, maxi))


    def printLevelOrder(self,root):
        def printLevel(lvl,root):
          if root:
            if(lvl == 0):
                print(root.value,end=" ")
            printLevel(lvl-1,root.left)
            printLevel(lvl-1,root.right)

        h= self.height(self.root)
        print("Level order of this tree of height ",h)
        for i in range(0,h):
            printLevel(lvl=i,root=self.root)
            print('\n')

    def find(self,node,key):
        found = False
        if node:
            if key == node.value:
                found = True
                return True
            elif key < node.value:
                self.find(node.left,key)
            else:
                self.find(node.right,key)
        return found




if __name__ == '__main__':
    bst = BST()

    for i in range(10):
        ele = randint(1, 100)
        print(ele,end=' ')
        bst.add(ele)

    print("\n INORDER ->", end=' ')
    print (bst)

    # bst.get_preorder(bst.root)
    print(bst.height(bst.root))
    bst.printLevelOrder(bst.root)
    bst.add(33)
    # print(bst.find("Finding 33 in BST ",bst.find(bst.root,33)))

    print("Is this Tree BST? ", bst.isBST(bst.root))

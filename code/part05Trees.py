from rich import print
from rich.padding import Padding


class BinaryTree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def addElement(self, newData):
        # if out tree have a root node
        if self.data is not None:

            # creating left subtree:
            if newData < self.data:
                if self.left is None:
                    self.left = BinaryTree(newData)
                else:
                    self.left.addElement(newData)

            # creating right subtree:
            elif newData > self.data:
                if self.right is None:
                    self.right = BinaryTree(newData)
                else:
                    self.right.addElement(newData)

        # if we haven't node root, the 'newData'
        # will be the node root!
        else:
            self.data = newData

    def quantNodes(self) -> int:
        if self.data is None:
            return 0
        else:
            return 1 + quantNodes(self.left) + quantNodes(self.right)

    def levelBinaryTree(self):
        if self.data is None:
            return 0
        else:
            return max(levelBinaryTree(self.left), levelBinaryTree(self.right))

    # defining nodes position
    def gotOxy(self, line, column):
        print(Padding(self.data, (line, column)))

    # show our binary tree complete
    def showAllBinaryTree(self):
        if self.data is not None:
            line, column = 60, 2
            print(Padding(self.data, (60, 2)))
            self.left.showSubtreeLeft(self.data, line + 3, (column - (column / 2)))
            self.right.showSubtreeRight(self.data, line + 3, (column + (column / 2)))
        else:
            print("Binary Tree Empty", (50, 5))

    def showSubtreeLeft(self, line: int, column: int):
        if self.data is not None:
            print(Padding(self.data, (50, 3)))
            # gotOxy(50, 3)
            self.left.showSubtreeLeft(self.data, line + 3, column - 10)
            self.right.showSubtreeLeft(self.data, line + 3, column + 10)

    def showSubtreeRight(self, line: int, column: int):
        if self.data is not None:
            print(Padding(self.data, (70, 3)))
            # gotOxy(70, 3)
            self.left.showSubtreeRight(self.data, line + 3, column - 10)
            self.right.showSubtreeRight(self.data, line + 3, column + 10)

    # Display Order: root -> subtree right -> subtree left
    def showBTPreOrder(self):
        print(self.data, end=" ")

        if self.left:
            self.left.showBTPreOrder()

        if self.right:
            self.right.showBTPreOrder()

    # Display Order: subtree left -> root -> subtree right
    def showBTInOrder(self):
        if self.left:
            self.left.showBTInOrder()

        print(self.data, end=" ")

        if self.right:
            self.right.showBTInOrder()

    # Display Order: subtree left -> subtree right -> root
    def showBTPostOrder(self):
        if self.left:
            self.left.showBTPostOrder()

        if self.right:
            self.right.showBTPostOrder()

        print(self.data, end=" ")

    def searchElement(self, newData):
        # if our BT is Empty
        if self.data is None:
            return False

        # searching element in left subtree
        elif newData < self.data:
            if self.left is None:
                return "Element Not Found"
            return self.left.searchElement(newData)

        # searching element in right subtree
        elif newData > self.data:
            if self.right is None:
                return "Element Not Found"
            return self.right.searchElement(newData)

        # if newData is contained in BT
        else:
            return "Element Found"


tree = BinaryTree(10)

# creating our binary tree
tree.addElement(8)
tree.addElement(12)
tree.addElement(6)
tree.addElement(14)
tree.addElement(9)
tree.addElement(13)

print(end="\n")
tree.showBTPreOrder()
# output: 10 8 6 12 14

print(end="\n")
tree.showBTInOrder()
# output: 6 8 10 12 14

print(end="\n")
tree.showBTPostOrder()
# output: 6 8 14 12 10

# testing function search
print("\n")
print(tree.searchElement(6))
print(tree.searchElement(12))
print(tree.searchElement(15))
print(tree.searchElement(1))
"""
output:

Element Found
Element Found
Element Not Found
Element Not Found
"""

# show the binary tree
# showAllBinaryTree() -> it's not ok

# checking size of tree:
tree.quantNodes()

# checking level tree:
tree.levelBinaryTree()

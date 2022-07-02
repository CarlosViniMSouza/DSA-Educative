class LinkedList:
    def __init__(self, data=None) -> None:
        self.data = data
        self.nextData = None
        self.headData = None

    def addElement(self, newData):
        node = LinkedList(newData)  # creating a new node

        # If our linked list is empty, the 1° element is the HEAD:
        if node.headData is None:
            node.nextData = node
            return 0

        # lastData is very important:
        lastData = self.headData

        # lastData will loop through our linked list:
        while lastData is not None:
            lastData = self.nextData

        # The node with 'newData' is the last element
        lastData = node
        self.nextData = lastData

    def removeElement(self, newData):
        pass

    def searchElement(self, newData):
        pass

    def showLinkedList(self):
        pass

    def sizeLinkedList(self):
        pass


ll = LinkedList()

# building the linked list
ll.addElement(1)
ll.addElement(2)
ll.addElement(3)
ll.addElement(5)
ll.addElement(8)

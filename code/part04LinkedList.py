class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.nextData = None
        self.headData = None

    def addElementAtStart(self, newData):
        node = LinkedList(newData)

        # The last element will be principal
        node.nextData = self.headData

        # The principal element is node
        self.headData = node

    def addElementAtLast(self, newData):
        node = LinkedList(newData)  # creating a new node

        # If our linked list is empty, the 1° element is the HEAD:
        if self.headData is None:
            self.headData = node
            return 0

        # lastData is very important:
        lastData = self.headData

        # lastData will loop through our linked list:
        while lastData.nextData is not None:
            lastData = lastData.nextData

        # The node with 'newData' is the last element
        lastData.nextData = node

    def removeElement(self, newData):
        pass

    def searchElement(self, newData):
        pass

    def showLinkedList(self):
        node = self.headData

        while node is not None:
            print(node.data, end=" ")
            node = node.nextData
        print(end="\n")

    def sizeLinkedList(self):
        node = self.headData
        cont = 0

        # cont will before of node.nextData
        # because need counted the 'headData'
        while node is not None:
            cont += 1
            node = node.nextData

        print("\nThe linked list size:", cont)


ll = LinkedList()

# building the linked list
ll.addElementAtLast(1)
ll.addElementAtLast(2)
ll.addElementAtLast(3)
ll.addElementAtLast(5)
ll.addElementAtLast(8)

# show the linked list:
ll.showLinkedList()

# check the size:
ll.sizeLinkedList()

class Node:
    def __init__(self) -> None:
        self.data = None
        self.nextData = None


class LinkedList:
    def __init__(self) -> None:
        self.headData = None


ll = LinkedList()

ll.headData = Node(1)

ll.headData.nextData = Node(2)
ll.headData.nextData = Node(3)
ll.headData.nextData = Node(5)
ll.headData.nextData = Node(8)

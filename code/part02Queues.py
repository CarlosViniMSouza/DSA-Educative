from collections import deque


class Dequeue:
    def __init__(self) -> None:
        self.data = deque()

    def addElement(self, newData) -> None:
        self.data.append(newData)

    def addElementLeft(self, newData) -> None:
        self.data.appendleft(newData)

    def removeElementLeft(self) -> None:
        self.data.popleft()

    def removeElementRigth(self) -> None:
        self.data.pop()

    def searchElement(self, newData) -> str:
        for i in self.data:
            if newData == i:
                return f"Element Found: {newData}"
            return "Element Not Found"

    def reverseKElements(self, newData):
        # ex.: 1, 2, 3, 4, 5, 6, 7 (reverse 4 numbers):
        # res.: 4, 3, 2, 1, 5, 6, 7 (concluded)
        listrev = deque()

        for i in range(0, newData):
            listrev.append(self.data[i])
            i += 1

        for j in range(0, newData):
            self.data.popleft()
            j += 1

        listrev.reverse()

        print("New List:", listrev + self.data)

    def showDequeue(self) -> deque:
        print(self.data)


deq = Dequeue()

# adding elements (for right)
deq.addElement(4)
deq.addElement(5)
deq.addElement(6)
deq.addElement(7)

# adding elements (for left)
deq.addElementLeft(3)
deq.addElementLeft(2)
deq.addElementLeft(1)

# see how to my deque
deq.showDequeue()

# removing 1 element in left
# removing 1 element in left
deq.removeElementLeft()
deq.removeElementRigth()

# see the new deque
deq.showDequeue()

# applied the reverse K elements:
deq.reverseKElements(3)  # problems!!

class Stack:
    def __init__(self) -> None:
        self.data = []

    def addElement(self, newData):
        self.data.append(newData)

    def addElementBelow(self, newData):
        self.data.insert(0, newData)

    def removeElement(self):
        self.data.pop()

    def removeElementBelow(self):
        self.data.pop(0)

    def searchElement(self, newData):
        if newData == self.data:
            print(f"Element found: {newData}")
        else:
            print("Element Not Found")

    def sizeStack(self):
        print(f"The size is: {len(self.data)}")

    def reverseKElements(self, newData):
        stackrev = []

        for i in range(0, newData):
            stackrev.append(self.data[i])
            i += 1

        for j in range(0, newData):
            self.data.pop(0)
            j += 1

        stackrev.reverse()

        print("The new Stack:", stackrev + self.data)

    def showStack(self):
        for i in self.data:
            print(i)

    def showStackList(self):
        print(self.data)


stack = Stack()

# adding elemets:
stack.addElement(4)
stack.addElement(3)
stack.addElement(2)
stack.addElementBelow(5)
stack.addElementBelow(6)
stack.addElementBelow(7)

# show stack:
stack.showStack()
print("\n")

# removing 2 elements:
stack.removeElement()  # remove '2'
stack.removeElementBelow()  # remove '7'

# see the actual stack:
stack.showStack()
print("\n")

# searching 2 elements:
stack.searchElement(5)
stack.searchElement(10)

# size stack:
stack.sizeStack()
stack.showStackList()

# reverse 3 elements:
stack.reverseKElements(3)

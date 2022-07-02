class Stack:
    def __init__(self) -> None:
        self.data = []

    def addElement(self, newData):
        self.data.append(newData)

    def addElementBelow(self, newData):
        self.data.insert(0, newData)

    def removeElement(self):
        if self.data is not None:
            self.data.pop()
        else:
            print("\nStack Empty! Add an element")

    def removeElementBelow(self):
        if self.data is not None:
            self.data.pop(0)
        else:
            print("\nStack Empty! Add an element")

    def searchElement(self, newData):
        if self.data is not None:
            if newData in self.data:
                print(f"\nElement Found: {newData}")
            else:
                print("\nElement Not Found")
        else:
            print("\nStack Empty!!")

    def sizeStack(self):
        print(f"\nThe size is: {len(self.data)}")

    def reverseKElements(self, newData):
        stackrev = []

        for i in range(0, newData):
            stackrev.append(self.data[i])
            i += 1

        for j in range(0, newData):
            self.data.pop(0)
            j += 1

        stackrev.reverse()

        print("\nThe new Stack:", stackrev + self.data)

    def showStack(self):
        for i in self.data:
            print(f"[{i}]")

    def showStackList(self):
        print(f"\n{self.data}")


stack = Stack()

# adding elemets:
stack.addElement(4)
stack.addElement(3)
stack.addElement(2)
stack.addElement(1)
stack.addElementBelow(5)
stack.addElementBelow(6)
stack.addElementBelow(7)
stack.addElementBelow(8)

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
stack.searchElement(4)
stack.searchElement(10)

# size stack:
stack.sizeStack()
stack.showStackList()

# reverse 3 elements:
stack.reverseKElements(3)

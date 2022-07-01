class structList:
    def __init__(self):
        self.listTest01 = list()
        self.listTest02 = list()

    def addNumbersList01(self, newData):
        self.listTest01.append(int(newData))

    def addNumbersList02(self, newData):
        self.listTest02.append(int(newData))

    def removeNumsList01(self, newData):
        if newData is self.listTest01:
            self.listTest01.remove(newData)
        else:
            return "Element not exist in list01"

    def removeNumsList02(self, newData):
        if newData is self.listTest02:
            self.listTest02.remove(newData)
        else:
            return "Element not exist in list02"

    def mergeTwoLists(self):
        return self.listTest01 + self.listTest02

    def findMinValue(self):
        print(f"\nMinimun Value of List01: {min(self.listTest01)}")
        print(f"\nMinimun Value of List02: {min(self.listTest02)}")

    def maxSumSublist(self):
        print("\nSummation:", sum(self.listTest01) + sum(self.listTest02))

    def productAllElements(self):
        prod = 1

        for i in self.listTest01:
            prod *= i
        print(f"\nElements List01(Product): {prod}")

        prod = 1  # return 'prod' to state 1

        for j in self.listTest02:
            prod *= j
        print(f"\nElements List02(Product): {prod}")

    def searchElement(self, newData):
        for i in self.listTest01:
            if newData == i:
                print("\nElement founded in list01")

        for j in self.listTest02:
            if newData == j:
                print("\nElement founded in list02")

        return "\nElement Not founded on lists"


studyList = structList()

# Creating list01:
studyList.addNumbersList01(4)
studyList.addNumbersList01(6)
studyList.addNumbersList01(8)
studyList.addNumbersList01(10)

# Creating list02:
studyList.addNumbersList02(3)
studyList.addNumbersList02(5)
studyList.addNumbersList02(7)
studyList.addNumbersList02(9)

# Removing 1 element to list01:
studyList.removeNumsList01(1)

# Removing 1 element to list02:
studyList.removeNumsList02(1)

# Merge the 2 lists:
studyList.mergeTwoLists()

# Find Minimun Value of lists:
studyList.findMinValue()

# Maximun Sum Sublists:
studyList.maxSumSublist()

# Product all elements of lists:
studyList.productAllElements()

# Search Elements:
studyList.searchElement(0)
